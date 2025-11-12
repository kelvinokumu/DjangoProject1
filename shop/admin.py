from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}  # auto-fills slug from name
    ordering = ['name']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'created', 'updated']
    list_filter = ['category', 'created', 'updated']
    search_fields = ['name', 'description']


admin.site.site_header = "My Shop Administration"
# admin.site.site_title = "My Shop Admin Portal"
admin.site.index_title = "Welcome to My Shop Dashboard"