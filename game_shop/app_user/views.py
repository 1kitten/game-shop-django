from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect
from django import views
from django.views import generic
from .forms import RegisterForm, BalanceForm
from .models import Profile
import logging

logger = logging.getLogger(__name__)


class RegisterView(views.View):
    def get(self, request):
        logger.info('была получена страница с регистрацией')
        registration_form = RegisterForm()
        return render(request, 'user/register.html', {'form': registration_form})

    def post(self, request):
        registration_form = RegisterForm(request.POST)
        if registration_form.is_valid():
            user = registration_form.save()
            Profile.objects.create(
                user=user,
            )
            login(request, user)
            return redirect('/')
        return render(request, 'user/register.html', {'form': registration_form})


class UserProfileView(generic.DetailView):
    model = Profile
    template_name = 'user/profile.html'
    context_object_name = 'profile'


class AuthenticateView(LoginView):
    template_name = 'user/login.html'


class SignOutView(LogoutView):
    next_page = '/'


class UserBalanceView(views.View):
    def get(self, request, pk):
        if pk != request.user.id:
            raise PermissionDenied
        balance_form = BalanceForm()
        return render(request, 'user/balance.html', {'form': balance_form})

    def post(self, request, pk):
        balance_form = BalanceForm(request.POST)
        if balance_form.is_valid():
            amount = balance_form.cleaned_data.get('amount')
            user_profile = Profile.objects.filter(id=request.user.id).first()
            user_profile.balance += int(amount)
            user_profile.save()
            return redirect('/')
        return render(request, 'user/balance.html', {'form': balance_form})

