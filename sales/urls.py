

from django.urls import path
from .import views

urlpatterns = [
   
    path('login',views.login),
    path('registration',views.registration),
    path('user-list',views.userList),
    path('category-list',views.categoryList),
    path('category_edit/<int:pk>',views.category_edit,name='edit'),
    path('category_delete/<int:pk>',views.category_delete,name='delete'),
    path('product-list',views.productList),
    path('product_edit/<int:pk>',views.product_edit,name='edit'),
    path('product_delete/<int:pk>',views.product_delete,name='delete'),
]
