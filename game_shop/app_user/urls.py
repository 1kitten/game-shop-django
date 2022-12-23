from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register_user'),
    path('login/', views.AuthenticateView.as_view(), name='login'),
    path('logout/', views.SignOutView.as_view(), name='logout'),
    path('<int:pk>/', views.UserProfileView.as_view(), name='user_profile'),
    path('balance/<int:pk>/', views.UserBalanceView.as_view(), name='get_balance'),
]
