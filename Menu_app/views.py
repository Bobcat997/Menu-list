from django.shortcuts import render
from menu_app import models
from .forms import DishesForm, MenuForm
from django.contrib import messages


def index(request):
    menus = models.Menu.objects.all()
    return render(request, 'index.html', {"menus": menus, })


def menu_add(request):
    form = MenuForm()

    if request.method == 'POST':
        form = MenuForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Menu added")

    context = {'form': form}
    return render(request, 'menu_add.html', context)


def dishes_add(request):
    form = DishesForm()

    if request.method == 'POST':
        form = DishesForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Dishes added")

    context = {'form': form}
    return render(request, 'dishes_add.html', context)
