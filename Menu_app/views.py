from django.shortcuts import render, redirect
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


def DeleteMenu(request, id):
    menu = models.Menu.objects.get(pk=id)
    menu.delete()
    return redirect('/menu_app')


def UpdateMenu(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = MenuForm()
        else:
            menu = models.Menu.objects.get(pk=id)
            form = MenuForm(instance=menu)
        return render(request, "menu_add.html", {'form': form})
    else:
        if id == 0:
            form = MenuForm(request.POST)
        else:
            menu = models.Menu.objects.get(pk=id)
            form = MenuForm(request.POST, instance=menu)
        if form.is_valid():
            form.save()
        return redirect('/menu_app')
