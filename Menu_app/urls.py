from django.urls import path, include
from menu_app import views

urlpatterns = [
    path('menu_app/', views.index, name='index'),
    path('menu_add/', views.menu_add, name="menu_add"),
    path('dishes_add/', views.dishes_add, name="dishes_add")

]
