from .models import Profile


def decrease_user_balance(user_id, amount):
    user = Profile.objects.get(user_id=user_id)
    if user:
        user.balance -= amount
    user.save()


def increase_user_money_spent(user_id, amount):
    user = Profile.objects.get(user_id=user_id)
    if user:
        user.money_spent += amount
    user.save()


def check_user_royalty(user_id):
    user = Profile.objects.get(user_id=user_id)
    if user:
        if 1000 <= user.money_spent < 5000:
            user.royalty_id = '1'
        elif 5000 <= user.money_spent < 7000:
            user.royalty_id = '2'
        elif 7000 <= user.money_spent < 9000:
            user.royalty_id = '3'
        elif 9000 <= user.money_spent < 15000:
            user.royalty_id = '4'
        elif 15000 <= user.money_spent:
            user.royalty_id = '5'
    user.save()
