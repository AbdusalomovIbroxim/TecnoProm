from django.test import TestCase
from django.urls import reverse
from .models import Country, City, Categories, SubCategories, Tag, Products
import uuid


class CountryModelTest(TestCase):
    def setUp(self):
        self.country = Country.objects.create(
            slug=uuid.uuid4(),
            name_en="USA",
            name_ru="США",
            name_uz="AQSH"
        )

    def test_country_creation(self):
        self.assertEqual(str(self.country), "AQSH")  # Так как в тесте используется язык по умолчанию (узбекский)

    def test_country_url(self):
        url = self.country.get_absolute_url()
        self.assertEqual(url, reverse("country_detail", kwargs={"slug": self.country.slug}))


class CityModelTest(TestCase):
    def setUp(self):
        self.country = Country.objects.create(
            slug=uuid.uuid4(),
            name_en="USA",
            name_ru="США",
            name_uz="AQSH"
        )
        self.city = City.objects.create(
            slug=uuid.uuid4(),
            country=self.country,
            name="New York"
        )

    def test_city_creation(self):
        self.assertEqual(str(self.city), "New York")

    def test_city_url(self):
        url = self.city.get_absolute_url()
        self.assertEqual(url, reverse("city_detail", kwargs={"slug": self.city.slug}))


class CategoryModelTest(TestCase):
    def setUp(self):
        self.category = Categories.objects.create(
            slug=uuid.uuid4(),
            name_en="Electronics",
            name_ru="Электроника",
            name_uz="Elektronika"
        )

    def test_category_creation(self):
        self.assertEqual(str(self.category), "Elektronika")

    def test_category_url(self):
        url = self.category.get_absolute_url()
        self.assertEqual(url, reverse("category_detail", kwargs={"slug": self.category.slug}))


class SubCategoryModelTest(TestCase):
    def setUp(self):
        self.category = Categories.objects.create(
            slug=uuid.uuid4(),
            name_en="Electronics",
            name_ru="Электроника",
            name_uz="Elektronika"
        )
        self.subcategory = SubCategories.objects.create(
            slug=uuid.uuid4(),
            name_en="Mobile Phones",
            name_ru="Мобильные телефоны",
            name_uz="Mobil telefonlar"
        )

    def test_subcategory_creation(self):
        self.assertEqual(str(self.subcategory), "Mobil telefonlar")

    def test_subcategory_url(self):
        url = self.subcategory.get_absolute_url()
        self.assertEqual(url, reverse("subcategory_detail", kwargs={"slug": self.subcategory.slug}))


class TagModelTest(TestCase):
    def setUp(self):
        self.tag = Tag.objects.create(
            name_en="Smartphones",
            name_ru="Смартфоны",
            name_uz="Smartfonlar"
        )

    def test_tag_creation(self):
        self.assertEqual(str(self.tag), "Smartfonlar")


class ProductModelTest(TestCase):
    def setUp(self):
        self.country = Country.objects.create(
            slug=uuid.uuid4(),
            name_en="USA",
            name_ru="США",
            name_uz="AQSH"
        )
        self.category = Categories.objects.create(
            slug=uuid.uuid4(),
            name_en="Electronics",
            name_ru="Электроника",
            name_uz="Elektronika"
        )
        self.product = Products.objects.create(
            slug=uuid.uuid4(),
            title="iPhone 12",
            description="Brand new iPhone 12 for sale",
            telephone="+123456789",
            country=self.country,
            category=self.category,
            price=999.99
        )

    def test_product_creation(self):
        self.assertEqual(str(self.product), "iPhone 12")

    def test_product_url(self):
        url = self.product.get_absolute_url()
        self.assertEqual(url, reverse("product-detail", kwargs={"slug": self.product.slug}))
