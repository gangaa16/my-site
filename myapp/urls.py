
""" from itertools import product
from xml.dom.minidom import Document
from django.conf import settings """
from django import views
from django.urls import path,include
from myapp.views import ProductDelete, ProductDetailView, ProductListView, ProductUpdateView, add_to_cart, index,new_one,products,product_details,add_product, show_cart,update_product,delete_product
app_name = 'myapp'
urlpatterns = [
    path('',index),
    path('new/',new_one),
    #path('products/',products,name = 'products'),
    path('products/',ProductListView.as_view(),name = 'products'),
    #path('products/<int:id>',product_details,name = 'product_details'),
    path('products/<int:pk>',ProductDetailView.as_view(),name = 'product_details'),
    
    path('products/add',add_product,name = 'add_product'),
    #path('products/update/<int:id>',update_product,name = 'update_product'),
    path('products/update/<int:pk>',ProductUpdateView.as_view(),name = 'update_product'),     
    #path('products/delete/<int:id>',delete_product,name = 'delete_product'),   
    path('products/delete/<int:pk>',ProductDelete.as_view(),name = 'delete_product'),
    path('products/<int:id>',add_to_cart, name='add-to-cart'),
    path('cart/',show_cart, name='showcart'),
]

