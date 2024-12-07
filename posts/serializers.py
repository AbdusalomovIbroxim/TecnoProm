import time, os
from rest_framework import serializers
from .models import Products, Image, Categories, SubCategories, Tag, Country, City


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    city = serializers.CharField(required=False, allow_null=True, allow_blank=True)
    images = ImageSerializer(many=True, read_only=True, source='image_set')
    # images = ImageSerializer(many=True, source='image_set')
    slug = serializers.CharField(read_only=True)

    class Meta:
        model = Products
        fields = ['pk', 'slug', 'title', 'description', 'telephone', 'telegram', 'country', 'city', 'category',
                  'subcategories', 'tags', 'images', 'create_date', 'type']

    def create(self, validated_data):
        request = self.context.get('request')
        product_type = request.data.get('type')
        subcategories_data = validated_data.pop('subcategories', [])
        tags_data = validated_data.pop('tags', [])

        images = self.initial_data.pop('images', []) if product_type == 'sell' else []

        product = Products.objects.create(**validated_data)

        product.subcategories.set(subcategories_data)
        product.tags.set(tags_data)

        if product_type == 'sell':
            product.type = "sell"
            product.save()
            for i, image in enumerate(images):
                timestamp = str(int(time.time()))
                file_name, ext = os.path.splitext(image.name)
                unique_name = f"{file_name}_{timestamp}_{i}{ext}"

                image.name = unique_name
                Image.objects.create(image=image, product=product)

        return product


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id', 'slug', 'name_en', 'name_ru', 'name_uz']


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['id', 'slug', 'country', 'name_en', 'name_ru', 'name_uz']


class CategorySerializer(serializers.ModelSerializer):
    icon = serializers.ImageField(read_only=True)
    
    class Meta:
        model = Categories
        fields = '__all__'


class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategories
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
