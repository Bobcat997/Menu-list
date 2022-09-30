from django.contrib import admin
from menu_app.models import Menu, Dish

myModels = [Menu, Dish]
admin.site.register(myModels)
