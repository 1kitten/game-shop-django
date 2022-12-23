from .models import Item


def decrease_item_stock(product_id, amount):
    item = Item.objects.get(id=product_id)
    if item:
        item.stock -= amount
    item.save()
