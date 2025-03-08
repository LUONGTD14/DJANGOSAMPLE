#serializer object help to convert to JSON when call API
from rest_framework import serializers
from .models import Category, Article, Feed

# Serializer cho Category
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        #view all field
        fields = '__all__'  

# Serializer cho Article
class ArticleSerializer(serializers.ModelSerializer):
    category = CategorySerializer()  # View detail category object instead of ID

    class Meta:
        model = Article
        fields = '__all__'

# Serializer cho Feed
class FeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feed
        fields = '__all__'
