from django.contrib import admin

# Register your models here.
from .models import Category
from .models import Article
from .models import Feed
from .define import ADMIN_SRC_CSS, ADMIN_SRC_JS, ADMIN_HEADER_NAME


#manager on admin
class CategoryAdmin(admin.ModelAdmin):
    # display field on table in django admin
    list_display = ('name', 'status', 'ordering')
    # choose field  to filter
    list_filter = ('name', 'status', 'ordering', 'ordering')
    # searchb field
    search_fields = ('name',)
    #genarate slug
    #prepopulated_fields = {'slug' : ('name',)}
    # auto generate slug
    class Media: 
        js = ADMIN_SRC_JS
        css = ADMIN_SRC_CSS

#add model to admin site
admin.site.register(Category, CategoryAdmin)


#manager on admin
class ArticleAdmin(admin.ModelAdmin):
    # display field on table in django admin
    list_display = ('name', 'status', 'ordering')
    # choose field  to filter
    list_filter = ('name', 'status', 'ordering')
    # searchb field
    search_fields = ('name',)
    # auto generate slug
    class Media: 
        js = ADMIN_SRC_JS
        css = ADMIN_SRC_CSS
#add model to admin site
admin.site.register(Article, ArticleAdmin)



class FeedAdmin(admin.ModelAdmin):
    # display field on table in django admin
    list_display = ('name', 'status', 'ordering')
    # choose field  to filter
    list_filter = ('name', 'status', 'ordering')
    # searchb field
    search_fields = ('name',)
    # auto generate slug
    class Media: 
        js = ADMIN_SRC_JS

#add model to admin site
admin.site.register(Feed, FeedAdmin)

#change header admin page name from default to my name
admin.site.site_header = ADMIN_HEADER_NAME