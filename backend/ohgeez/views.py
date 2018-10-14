from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.views.generic.edit import FormView
from django.views.generic import DetailView
from django.urls import reverse_lazy

from .models import Category
from .models import Item

from .forms import ItemForm

class CategoryListView(ListView):
    model = Category
    template_name = 'ohgeez/index.html'


class ItemListView(ListView):
    model = Item
    paginate_by = 10

    def get_queryset(self):
        if 'category' in self.kwargs:
            category = self.kwargs['category']
            return Item.objects.filter(category__pk=category)
        else:
            return Item.objects.all()

class CreateItemView(FormView):
    template_name = 'ohgeez/add.html'
    form_class = ItemForm
    model = Item
    success_url = reverse_lazy('category-list')

class ItemDetailView(DetailView):
    model = Item
