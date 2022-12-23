from django.shortcuts import render
from django.views import generic
from .models import Item


class ItemsList(generic.ListView):
    model = Item
    paginate_by = 8
    context_object_name = 'items'
    template_name = 'shop/items_list.html'

    def get_queryset(self):
        return Item.objects.select_related('shop').all()


class ItemDetail(generic.DetailView):
    model = Item
    template_name = 'shop/item_detail.html'
    context_object_name = 'item'
