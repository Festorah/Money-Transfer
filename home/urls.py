from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('LogoutPage/', views.LogoutPage, name='LogoutPage'),
    path('LoginPage/', views.LoginPage, name='LoginPage'),
    path('send_money/', views.send_money, name='send-money'),
    path('confirm/', views.confirm, name='confirm'),
    path('money_sent/', views.money_sent, name='money-sent'),
    path('Login/', views.Login, name='Login'),
]
