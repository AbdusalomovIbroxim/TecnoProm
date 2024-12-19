from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny
from rest_framework import status, generics
from .models import Products, Categories, SubCategories, SubCategoryCategory, Tag, Country, City
from .serializers import (ProductSerializer, SubcategorySerializer, TagSerializer,
                          CategorySerializer, CountrySerializer, CitySerializer)
from .filters import ProductFilter
from rest_framework.pagination import PageNumberPagination
from drf_yasg.utils import swagger_auto_schema


class LatestProductsView(APIView):
    permission_classes = [AllowAny, ]

    def get(self, request):
        product_type = request.GET.get('type')
        print(product_type)
        if product_type not in ['buy', 'sell']:
            return Response({'detail': 'Некорректный тип продукта. Ожидалось "buy" или "sell".'},
                            status=status.HTTP_400_BAD_REQUEST)

        products = Products.objects.filter(type=product_type).order_by('-create_date')[:12]

        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


class CustomPagination(PageNumberPagination):
    page_size = 40
    page_size_query_param = 'page_size'
    max_page_size = 100


class PaginatedProductsView(APIView):
    def get(self, request):
        paginator = CustomPagination()
        products = Products.objects.all().order_by('-create_date')
        paginated_products = paginator.paginate_queryset(products, request)
        serializer = ProductSerializer(paginated_products, many=True)
        return paginator.get_paginated_response(serializer.data)


@swagger_auto_schema(
    method='post',
    request_body=ProductSerializer,
    responses={201: ProductSerializer, 400: 'Ошибка запроса'}
)
@api_view(['POST'])
def create_product(request):
    product_type = request.data.get('type')

    if product_type not in ['buy', 'sell']:
        return Response({'detail': 'Некорректный тип продукта. Ожидалось "buy" или "sell".'},
                        status=status.HTTP_400_BAD_REQUEST)

    if product_type == 'sell':
        if not request.user.is_authenticated:
            return Response({'detail': 'Требуется авторизация для добавления продукта на продажу.'},
                            status=status.HTTP_401_UNAUTHORIZED)

        currency = request.user.currency
        if currency < 10:
            return Response({'detail': 'Недостаточно баллов для добавления продукта на продажу.'},
                            status=status.HTTP_400_BAD_REQUEST)

        request.user.currency -= 10
        request.user.save()

    serializer = ProductSerializer(data=request.data, context={'request': request})
    if serializer.is_valid():
        if request.data['city'] == 'null':
            serializer.validated_data.pop('city', None)

        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductView(APIView):
    @swagger_auto_schema(
        responses={200: ProductSerializer()},
    )
    def get(self, request, slug):
        try:
            product = Products.objects.get(slug=slug)
            serializer = ProductSerializer(product)
            return Response(serializer.data)
        except Products.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(
        request_body=ProductSerializer,
        responses={200: ProductSerializer()},
    )
    def patch(self, request, slug):
        try:
            product = Products.objects.get(slug=slug)

            existing_images = product.image_set.all()
            images_in_request = request.data.get('images', [])

            if not images_in_request:
                request.data['images'] = [image.id for image in existing_images]

            serializer = ProductSerializer(product, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Products.DoesNotExist:
            return Response({'detail': 'Продукт не найден'}, status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(
        responses={204: 'No Content'}
    )
    def delete(self, request, slug):
        try:
            product = Products.objects.get(slug=slug)
            product.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Products.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class SimilarProductsView(APIView):
    def get(self, request, slug):
        try:
            product = Products.objects.get(slug=slug)
            similar_products = Products.objects.filter(category=product.category).exclude(slug=slug).order_by(
                '-create_date')[:5]
            serializer = ProductSerializer(similar_products, many=True)
            return Response(serializer.data)
        except Products.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class CategoryListView(APIView):
    def get(self, request):
        categories = Categories.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)


class SubcategoryDetailsView(generics.ListAPIView):
    queryset = SubCategories.objects.all()
    serializer_class = SubcategorySerializer

    def get_queryset(self):
        category_id = self.request.query_params.get('category_id')
        if category_id:
            subcategory_ids = SubCategoryCategory.objects.filter(category_id=category_id).values_list('subcategory_id',
                                                                                                      flat=True)
            return self.queryset.filter(id__in=subcategory_ids)
        return self.queryset.none()


class TagDetailsView(generics.ListAPIView):
    serializer_class = TagSerializer

    def get_queryset(self):
        queryset = Tag.objects.all()

        category_ids = self.request.query_params.getlist('category_id')
        subcategory_ids = self.request.query_params.getlist('subcategory_id')

        if category_ids:
            queryset = queryset.filter(category_tags__category__id__in=category_ids)

        if subcategory_ids:
            queryset = queryset.filter(subcategory_tags__subcategory__id__in=subcategory_ids)

        return queryset


class FilteredProductsView(generics.ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ProductFilter

    def get_queryset(self):
        queryset = super().get_queryset()
        sort = self.request.query_params.get('sort', 'newest')
        if sort == 'oldest':
            queryset = queryset.order_by('create_date')
        else:
            queryset = queryset.order_by('-create_date')
        return queryset


class CountryListView(generics.ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class CityListView(generics.ListAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
