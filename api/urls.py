from django.urls import path
from . import views

urlpatterns = [
	path('', views.apiOverview, name='apiOverview'),
	path('transaction_list/', views.transactionList, name='transaction-list'),
	path('transaction_detail/<str:pk>/', views.transactionDetial, name='transaction-detail'),
	path('profile_list/', views.profileList, name='profile-list'),
	path('profile_detail/<str:pk>/', views.profileDetail, name='profile-detail'),
	path('profile_create/', views.profileCreate, name='profile-create'),
	path('profile_update/<str:pk>/', views.profileUpdate, name='profile-update'),
	path('profile_delete/<str:pk>/', views.profileDelete, name='profile-delete'),
]
