from django.urls import path
from .views import (
    LatestProductsView,
    PaginatedProductsView,
    create_product,
    ProductView,
    SimilarProductsView,
    FilteredProductsView,
    CountryListView,
    CityListView,
    CategoryListView,
    SubcategoryDetailsView,
    TagDetailsView
)

urlpatterns = [
    path('filter/', FilteredProductsView.as_view(), name='filtered-products'),

    path('products/list', PaginatedProductsView.as_view(), name='paginated-products'),
    path('products/recent/', LatestProductsView.as_view(), name='latest-products'),

    # Группировка CRUD операций
    path('products/', create_product, name='product-create'),
    path('products/<slug:slug>/', ProductView.as_view(), name='product-detail'),
    path('products/<slug:slug>/similar/', SimilarProductsView.as_view(), name='similar-products'),  # Похожие продукты

    path('countries/', CountryListView.as_view(), name='country_list'),
    path('cities/', CityListView.as_view(), name='city_list'),
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('subcategories/', SubcategoryDetailsView.as_view(), name='subcategory-details'),
    path('tags/', TagDetailsView.as_view(), name='tag-details'),
]
