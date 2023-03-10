from django.views import generic
from .models import Item
from cart.forms import CartAddProductForm
import logging

logger = logging.getLogger(__name__)


class ItemsList(generic.ListView):
    model = Item
    paginate_by = 8
    context_object_name = 'items'
    template_name = 'shop/items_list.html'

    def get_queryset(self):
        logger.debug('Была вызвана страница со списком игр')
        return Item.objects.select_related('shop').all()


class ItemDetail(generic.DetailView):
    model = Item
    template_name = 'shop/item_detail.html'
    context_object_name = 'item'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart_product_form'] = CartAddProductForm()
        return context
