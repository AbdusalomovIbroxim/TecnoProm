# from django.forms import ModelMultipleChoiceField
# from django import forms
from django.contrib import admin
# from django.contrib.admin.widgets import FilteredSelectMultiple

from .models import Categories, Products, SubCategories, Country, City, Tag, TagCategory, TagSubcategory, \
    SubCategoryCategory, Image


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ("slug", "name_uz", "name_ru", "name_en")
    prepopulated_fields = {'slug': ('name_en',)}


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ("slug", "name_uz", "name_ru", "name_en")
    prepopulated_fields = {'slug': ('name_en',)}


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ("slug", "name_uz", "name_ru", "name_en")
    prepopulated_fields = {'slug': ('name_en',)}


class SubcategoriesCategoryInline(admin.TabularInline):
    model = SubCategoryCategory
    extra = 1


@admin.register(SubCategories)
class TagsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_en', 'name_ru', 'name_uz')
    inlines = [SubcategoriesCategoryInline]
    prepopulated_fields = {'slug': ('name_en',)}


class TagsInline(admin.TabularInline):
    model = TagCategory
    extra = 1


class TagsSubcategoryInline(admin.TabularInline):
    model = TagSubcategory
    extra = 1


@admin.register(Tag)
class TagsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_en', 'name_ru', 'name_uz')
    inlines = [TagsInline, TagsSubcategoryInline]


# Inline для изображений
class ImageInline(admin.TabularInline):  # Можно использовать StackedInline для вертикального отображения
    model = Image
    extra = 1  # Количество пустых форм для добавления изображений
    fields = ('image',)  # Выбираем только поле для изображения

# Обновленный класс ProductsAdmin с изображениями
@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ("title", "create_date", "update_date", "is_published")
    list_filter = ("is_published",)
    search_fields = ("title",)
    prepopulated_fields = {'slug': ('title',)}
    
    inlines = [ImageInline]  # Добавляем Inline для изображений

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "sub_category":
            selected_category_id = request.POST.get("category")
            if selected_category_id:
                kwargs["queryset"] = SubCategories.objects.filter(category_id=selected_category_id)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)