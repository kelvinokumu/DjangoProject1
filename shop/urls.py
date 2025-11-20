from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('add-category/', views.add_category, name='add_category'),
    path('add-product/', views.add_product, name='add_product'),
    path('delete-category/<int:pk>/', views.delete_category, name='delete_category'),
    path('delete-product/<int:pk>/', views.delete_product, name='delete_product'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),


    # path('product/<int:id>/', views.product_detail, name='product_detail'),
    # path('product/add/', views.product_create, name='product_add'),
    # path('category/add/', views.category_create, name='category_add'),
]
