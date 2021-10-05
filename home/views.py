from django.shortcuts import render, redirect
from django.contrib.auth import login as django_login, authenticate, logout
from .forms import SignUpForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from .models import *




def home(request):
	return render(request, 'home/index.html')



def signup(request):

	form = SignUpForm()
	context = {'form': form}
	return render(request, 'home/signup.html', context)




def Login(request):
	if request.method == 'POST':
		form  = SignUpForm(request.POST)

		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password2')
			user = authenticate(request, username=username, password=password)
			if user is not None:
				django_login(request, user)
				return redirect('dashboard')
	context = {}
	return render(request, 'home/login.html', context)



def LoginPage(request):

	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request, username=username, password=password)
		if user is not None:
			django_login(request, user)
			return redirect('dashboard')
	context = {}
	return render(request, 'home/login.html', context)


@login_required(login_url='LoginPage')
def send_money(request):
	profiles = Profile.objects.all()
	context = {'profiles': profiles}

	return render(request, 'home/send_money.html', context)

@login_required(login_url='LoginPage')
def confirm(request):

	if request.method == 'POST':

		recipient_pk = request.POST.get('recipient_pk')
		amount = request.POST.get('amount')
		recipient_profile = Profile.objects.get(pk=recipient_pk)

		context = {'recipient_profile': recipient_profile, 'amount': amount}

		return render(request, 'home/confirm.html', context)

def money_sent(request):

	if request.method == 'POST':

		description = request.POST.get('description')
		recipient_profile = request.POST.get('recipient_pk')
		amount = request.POST.get('amount')

		recipient_profile = Profile.objects.get(pk=recipient_profile)
		recipient_profile.account_balance = int(recipient_profile.account_balance) + int(amount)
		recipient_profile.save()

		sender_profile = Profile.objects.get(user=request.user)
		sender_profile.account_balance = int(sender_profile.account_balance) - int(amount)
		sender_profile.save()

		transaction = Transaction.objects.create(sender=request.user, receiver=recipient_profile.user, description=description, amount=amount)

		context = {'recipient_profile': recipient_profile, 'amount': amount}

	return render(request, 'home/money_sent.html')



def LogoutPage(request):

	logout(request)
	return redirect('LoginPage')

@login_required(login_url='LoginPage')
def dashboard(request):
	sender = request.user
	transactions = sender.transaction_set.all()
	context = {'transactions': transactions}

	return render(request, 'home/dashboard.html', context)


