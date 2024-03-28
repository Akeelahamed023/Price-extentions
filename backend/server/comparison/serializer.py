from rest_framework import serializers

from .models import PhoneData, CategoryChoices, BrandChoices, ModelChoices

class CategoryChoicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryChoices
        fields = '__all__'

class BrandChoicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = BrandChoices
        fields = '__all__'

class ModelChoicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelChoices
        fields = '__all__'

class ComparisonSerializer(serializers.ModelSerializer):
    Category = CategoryChoicesSerializer()
    brand = BrandChoicesSerializer()
    model = ModelChoicesSerializer()

    class Meta:
        model = PhoneData
        fields = ['id', 'price', 'link', 'Category', 'brand', 'model']