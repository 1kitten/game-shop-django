from .models import Profile
import logging

logger = logging.getLogger('decreased_user_balance')
logger_status = logging.getLogger('user_status')


def decrease_user_balance(user_id, amount):
    user = Profile.objects.get(user_id=user_id)
    if user:
        user.balance -= amount
        logger.info('balance was decreased', extra={'user': user.user.username,
                                                    'amount': amount})
    user.save()


def increase_user_money_spent(user_id, amount):
    user = Profile.objects.get(user_id=user_id)
    if user:
        user.money_spent += amount
    user.save()


def check_user_royalty(user_id):
    user = Profile.objects.get(user_id=user_id)
    current_status = user.royalty_id
    if 1000 <= user.money_spent < 5000:
        user.royalty_id = '2'
    elif 5000 <= user.money_spent < 7000:
        user.royalty_id = '3'
    elif 7000 <= user.money_spent < 10000:
        user.royalty_id = '4'
    elif user.money_spent >= 10000:
        user.royalty_id = '5'
    if user.royalty_id != current_status:
        logger_status.info('status changed', extra={'user': user.user.username,
                                                    'from': current_status,
                                                    'to': user.royalty_id})
        user.save()
