from rest_framework import serializers
from .models import Product, ReviewRating, ProductGallery,Category, Variation, VariationManager

class ProductGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductGallery
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
    
    def get_all_images(self,obj):
        images = obj.ProductGallery.all()
        return ProductGallerySerializer(images, many=True).data
