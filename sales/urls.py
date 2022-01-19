

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
    #Complain
    path('complain-list',views.complainList),
    path('complain-create',views.complainCreate),
    path('complain_edit/<int:pk>',views.complain_edit,name='edit'),
    path('complain_delete/<int:pk>',views.complain_delete,name='delete'),
]
