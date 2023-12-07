from rest_framework import serializers
from .models import Category, Product, Review


class CategorySerializer(serializers.ModelSerializer):
    products_count = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ('id', 'name', 'products_count')

    def get_products_count(self, obj):
        return obj.products.count()


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'title', 'description', 'price', 'category')


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'text', 'product', 'stars')


class ProductReviewSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    average_rating = serializers.SerializerMethodField()

    def get_average_rating(self, obj):
        total_stars = sum(review.stars for review in obj.reviews.all())
        num_reviews = obj.reviews.count()
        if num_reviews > 0:
            return total_stars / num_reviews
        else:
            return 0.0

    class Meta:
        model = Product
        fields = ('id', 'title', 'description', 'price', 'category', 'is_active', 'reviews', 'average_rating')
