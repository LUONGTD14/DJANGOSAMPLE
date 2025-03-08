from django.db import models
from tinymce.models import HTMLField

import uuid

from .custom_field import CustomBooleanFeild
from .helper import get_file_path
from .define import APP_VALUE_LAYOUT_DEFAULT, APP_VALUE_STATUS_DEFAULT
from .define import APP_VALUE_LAYOUT_CHOICE, APP_VALUE_STATUS_CHOICE
from .define import TABLE_ARTICLE_SHOW, TABLE_CATEGORY_SHOW, TABLE_FEED_SHOW

# Create your models here.
#Category model - table
class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(unique=True, max_length=100)
    slug = models.SlugField(unique=True, max_length=100)
    is_homePage = CustomBooleanFeild()
    layout = models.CharField(max_length=10, choices=APP_VALUE_LAYOUT_CHOICE, default=APP_VALUE_LAYOUT_DEFAULT)
    status = models.CharField(max_length=10, choices=APP_VALUE_STATUS_CHOICE, default=APP_VALUE_STATUS_DEFAULT)
    ordering = models.IntegerField(default=0)

    #define some things in admin site or database
    class Meta:
        #name of model in admin site
        verbose_name_plural = TABLE_CATEGORY_SHOW
    
    #custom information django admim respone object -> object.name feild
    def __str__ (self):
        return self.name

#Category model - table
class Article(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(unique=True, max_length=100)
    slug = models.SlugField(unique=True, max_length=100)
    status = models.CharField(max_length=10, choices=APP_VALUE_STATUS_CHOICE, default=APP_VALUE_STATUS_DEFAULT)
    ordering = models.IntegerField(default=0)
    special = CustomBooleanFeild()
    publish_date = models.DateTimeField()
    content = HTMLField()
    image = models.ImageField(upload_to=get_file_path)
    # foreign key to Category class, be deleted when Category deleted
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    #define some things in admin site or database
    class Meta:
        #name of model in admin site
        verbose_name_plural = TABLE_ARTICLE_SHOW

    #custom information django admim respone object -> object.name feild
    def __str__ (self):
        return self.name
    
#Category model - table
class Feed(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(unique=True, max_length=100)
    slug = models.SlugField(unique=True, max_length=100)
    status = models.CharField(max_length=10, choices=APP_VALUE_STATUS_CHOICE, default=APP_VALUE_STATUS_DEFAULT)
    ordering = models.IntegerField(default=0)
    link = models.CharField(max_length=250)

    #define some things in admin site or database
    class Meta:
        #name of model in admin site
        verbose_name_plural = TABLE_FEED_SHOW

    #custom information django admim respone object -> object.name feild
    def __str__ (self):
        return self.name