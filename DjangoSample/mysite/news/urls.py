from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ArticleViewSet, FeedViewSet

# create router auto generate endpoint API for viewset model
router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'articles', ArticleViewSet)
router.register(r'feeds', FeedViewSet)

urlpatterns = [
    path('api/', include(router.urls)),  # API endpoint start /api/
]
