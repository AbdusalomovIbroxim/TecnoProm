from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status, generics
from .models import Products, Categories, SubCategories, SubCategoryCategory, Tag, Country, City
from .serializers import ProductSerializer, SubcategorySerializer, TagSerializer, CategorySerializer, CountrySerializer, CitySerializer
from .filters import ProductFilter
from rest_framework.pagination import PageNumberPagination
from django.db.models import Q


# Пагинация
class CustomPagination(PageNumberPagination):
    page_size = 40
    page_size_query_param = 'page_size'
    max_page_size = 100

# Вывод последних 15 продуктов типа "купить"
class LatestProductsView(APIView):
    def get(self, request):
        # Получаем тип продукта из запроса
        product_type = request.GET.get('type')

        # Проверяем валидность типа продукта
        if product_type not in ['buy', 'sell']:
            return Response({'detail': 'Некорректный тип продукта. Ожидалось "buy" или "sell".'},
                            status=status.HTTP_400_BAD_REQUEST)

        # Фильтруем продукты по типу и сортируем по дате
        products = Products.objects.filter(type=product_type).order_by('-create_date')[:15]

        # Сериализуем данные
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


# Вывод всех продуктов с пагинацией по 40 продуктов
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

    serializer = ProductSerializer(data=request.data, context={'request': request})

    if product_type == 'sell':
        if not request.user.is_authenticated:
            return Response({'detail': 'Требуется авторизация для добавления продукта на продажу.'},
                            status=status.HTTP_401_UNAUTHORIZED)

        user_wallet_balance = request.user.wallet_balance
        if user_wallet_balance < 10:
            return Response({'detail': 'Недостаточно баллов для добавления продукта на продажу.'},
                            status=status.HTTP_400_BAD_REQUEST)

        request.user.wallet_balance -= 10
        request.user.save()

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# CRUD операции для продуктов
class ProductView(APIView):
    def get(self, request, slug):
        try:
            product = Products.objects.get(slug=slug)
            serializer = ProductSerializer(product)
            return Response(serializer.data)
        except Products.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, slug):
        try:
            product = Products.objects.get(slug=slug)
            serializer = ProductSerializer(product, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Products.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

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
            subcategory_ids = SubCategoryCategory.objects.filter(category_id=category_id).values_list('subcategory_id', flat=True)
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

    # Установите сортировку по умолчанию, если необходимо
    def get_queryset(self):
        queryset = super().get_queryset()
        # Установите сортировку по умолчанию, если фильтр не был применен
        sort = self.request.query_params.get('sort', 'newest')
        if sort == 'oldest':
            queryset = queryset.order_by('create_date')
        else:
            queryset = queryset.order_by('-create_date')
        return queryset

# class FilteredProductsView(APIView):
#     @swagger_auto_schema(
#         manual_parameters=[
#             openapi.Parameter('subcategory', openapi.IN_QUERY, description="ID подкатегории",
#                               type=openapi.TYPE_INTEGER),
#             openapi.Parameter('tag', openapi.IN_QUERY, description="ID тега", type=openapi.TYPE_INTEGER),
#             openapi.Parameter('latest', openapi.IN_QUERY, description="Сортировка по новизне (true/false)",
#                               type=openapi.TYPE_BOOLEAN),
#             openapi.Parameter('oldest', openapi.IN_QUERY, description="Сортировка по старине (true/false)",
#                               type=openapi.TYPE_BOOLEAN),
#             # Добавьте другие параметры фильтрации, если необходимо
#         ],
#         responses={
#             200: ProductSerializer(many=True),
#             400: 'Ошибка фильтрации',
#         }
#     )
#     def get(self, request):
#         filters = Q()
#         queryset = Products.objects.all()
#
#         # Применение фильтров
#         subcategory = request.GET.get('subcategory')
#         tag = request.GET.get('tag')
#         latest = request.GET.get('latest') == 'true'
#         oldest = request.GET.get('oldest') == 'true'
#
#         if subcategory:
#             filters &= Q(subcategories__id=subcategory)
#
#         if tag:
#             filters &= Q(tags__id=tag)
#
#         queryset = queryset.filter(filters)
#
#         # Сортировка
#         if latest:
#             queryset = queryset.order_by('-create_date')  # Сортировка по новизне
#         elif oldest:
#             queryset = queryset.order_by('create_date')  # Сортировка по старине
#
#         serializer = ProductSerializer(queryset, many=True)
#         return Response(serializer.data)

class CountryListView(generics.ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class CityListView(generics.ListAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer