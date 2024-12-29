from django.urls import path
from .views import (
    LatestProductsView,
    ProductsView,
    create_product,
    ProductView,
    SimilarProductsView, CountryListView, CityListView, CategoryListView, SubcategoryDetailsView, TagDetailsView,
)

urlpatterns = [
    path('products/', create_product, name='product-create'),
    path('products/list', ProductsView.as_view(), name='products-list'),
    path('products/recent/', LatestProductsView.as_view(), name='latest-products'),
    path('products/<slug:slug>/', ProductView.as_view(), name='product-detail'),
    path('products/<slug:slug>/similar/', SimilarProductsView.as_view(), name='similar-products'),  # Похожие продукты
    path('resources/countries/', CountryListView.as_view(), name='country_list'),
    path('resources/cities/', CityListView.as_view(), name='city_list'),
    path('resources/categories/', CategoryListView.as_view(), name='category_list'),
    path('resources/subcategories/', SubcategoryDetailsView.as_view(), name='subcategory_details'),
    path('resources/tags/', TagDetailsView.as_view(), name='tag_details'),
]
