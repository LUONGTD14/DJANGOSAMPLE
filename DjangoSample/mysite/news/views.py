from rest_framework import viewsets
from .models import Category, Article, Feed
from .serializers import CategorySerializer, ArticleSerializer, FeedSerializer

#using viewsets for support CRUD API on serializer object

# API for Category
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('ordering')  # sort by ordering
    serializer_class = CategorySerializer

# API for Article
class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all().order_by('-publish_date')  # sort by publish_date
    serializer_class = ArticleSerializer

# API for Feed
class FeedViewSet(viewsets.ModelViewSet):
    queryset = Feed.objects.all()
    serializer_class = FeedSerializer
