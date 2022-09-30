from django.urls import path, include
from menu_app import views

urlpatterns = [
    path('menu_app/', views.index, name='index'),

]
