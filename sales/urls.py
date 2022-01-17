

from django.urls import path
from .import views

urlpatterns = [
   
    path('login',views.login),
    path('registration',views.registration),
    path('user-list',views.userList),
    path('category-list',views.categoryList),
]
