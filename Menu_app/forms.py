from django.forms import ModelForm
from .models import Dish, Menu
from django import forms


class DishesForm(ModelForm):
    class Meta:
        model = Dish
        fields = '__all__'


class MenuForm(ModelForm):
    class Meta:
        model = Menu
        fields = '__all__'

    dishes = forms.ModelMultipleChoiceField(
        queryset=Dish.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
    )
