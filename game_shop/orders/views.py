from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from app_user.utils import decrease_user_balance, increase_user_money_spent, check_user_royalty
from app_shop.utils import decrease_item_stock
from django.db import transaction
from app_user.models import Profile


@transaction.atomic
def place_order(user_id, product_id, decrease_stock_value, user_money_value):
    decrease_user_balance(user_id, user_money_value)
    increase_user_money_spent(user_id, user_money_value)
    check_user_royalty(user_id)
    decrease_item_stock(product_id, decrease_stock_value)


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            user = Profile.objects.get(user_id=request.user.id)

            order = form.save()
            total = 0
            for item in cart:
                total += item['price']

            if total > user.balance:
                raise PermissionDenied

            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])

                place_order(user_id=request.user.id, product_id=item['product'].id,
                            decrease_stock_value=item['quantity'], user_money_value=item['price'])

            cart.clear()
            return render(request, 'orders/order/created.html',
                          {'order': order})
    else:
        form = OrderCreateForm
    return render(request, 'orders/order/create.html',
                  {'cart': cart, 'form': form})
