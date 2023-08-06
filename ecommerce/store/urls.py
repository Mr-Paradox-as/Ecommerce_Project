from django.urls import path, include

from . import views

urlpatterns = [
    path('',views.store,name='store'),
    #individual product
    path('product/<slug:slug>/', views.product_info, name='product-info'),
    #individual category
    path('search/<slug:category_slug>/', views.list_category, name='list-category'),

]