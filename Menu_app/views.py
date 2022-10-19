from django.shortcuts import render, redirect
from menu_app import models
from .forms import DishesForm, MenuForm
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import UpdateView, DeleteView, CreateView, ListView
from django.urls import reverse

# old approach


def index(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        if query:
            menus = models.Menu.objects.filter(name__icontains=query)
        else:
            menus = models.Menu.objects.all()
        return render(request, 'index.html', {"menus": menus, })


# def menu_add(request):
#     form = MenuForm()

#     if request.method == 'POST':
#         form = MenuForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Menu added")

#     context = {'form': form}
#     return render(request, 'menu_add.html', context)


# def dishes_add(request):
#     form = DishesForm()

#     if request.method == 'POST':
#         form = DishesForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Dishes added")

#     context = {'form': form}
#     return render(request, 'dishes_add.html', context)


# def DeleteMenu(request, id):
#     menu = models.Menu.objects.get(pk=id)
#     menu.delete()
#     return redirect('/menu_app')


# def UpdateMenu(request, id=0):
#     if request.method == "GET":
#         if id == 0:
#             form = MenuForm()
#         else:
#             menu = models.Menu.objects.get(pk=id)
#             form = MenuForm(instance=menu)
#         return render(request, "menu_add.html", {'form': form})
#     else:
#         if id == 0:
#             form = MenuForm(request.POST)
#         else:
#             menu = models.Menu.objects.get(pk=id)
#             form = MenuForm(request.POST, instance=menu)
#         if form.is_valid():
#             form.save()
#         return redirect('/menu_app')


class Index(ListView):
    model = models.Menu
    context_object_name = 'menus'
    template_name = 'index.html'
    paginate_by = 5

    def get_queryset(self):
        q = self.request.GET.get('q')
        if q:
            object_list = self.model.objects.filter(name__icontains=q)
        else:
            object_list = self.model.objects.all()
        return object_list


class DishesAdd(SuccessMessageMixin, CreateView):
    model = models.Menu
    form_class = DishesForm
    template_name = 'dishes_add.html'
    success_url = '/dishes_add/'
    success_message = 'Dishes Added'


class MenuAdd(SuccessMessageMixin, CreateView):
    model = models.Menu
    form_class = MenuForm
    template_name = 'menu_add.html'
    success_url = '/menu_add/'
    success_message = 'Menu Added'


class DeleteMenu(DeleteView):
    model = models.Menu
    template_name = "index.html"
    success_url = '/menu_app/'


class UpdateMenu(UpdateView):
    queryset = models.Menu.objects.all()
    template_name = 'menu_add.html'
    form_class = MenuForm
    success_url = '/menu_app/'
