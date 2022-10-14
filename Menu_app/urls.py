from django.urls import path, include
from menu_app import views

urlpatterns = [
    path('menu_app/', views.index.as_view(), name='index'),
    path('menu_add/', views.MenuAdd.as_view(), name="menu_add"),
    path('dishes_add/', views.DishesAdd.as_view(), name="dishes_add"),
    path('delete/<int:pk>/', views.DeleteMenu.as_view(), name='DeleteMenu'),
    path('<int:pk>/', views.UpdateMenu.as_view(), name='UpdateMenu'),
]
