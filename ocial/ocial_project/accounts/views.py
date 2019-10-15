from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from topics.models import *
from .models import *





def signup(request):
	if request.method == 'POST':
		if request.POST['password'] and request.POST['username'] and request.POST['email']:
			if request.POST['password'] == request.POST['password2']:
				try:
					user = User.objects.get(username = request.POST['username'])
					return render(request, 'accounts/signup.html', {'error': 'Username has already been taken'})
				except:
					try:
						user = User.objects.get(email = request.POST['email'])
						return render(request, 'accounts/signup.html', {'error': 'E-Mail is used by other user.'})
					except User.DoesNotExist:
						user = User.objects.create_user(request.POST['username'], password = request.POST['password'], email = request.POST['email'],first_name = request.POST['firstname'],last_name = request.POST['lastname'])
						auth.login(request,user)
						return redirect('home') 
			else:
				return render(request, 'accounts/signup.html', {'error': 'Password must match'})
		else:
			return render(request, 'accounts/signup.html', {'error': 'Username, E-Mail or Password cannot be empty.'})
	else:
		return render(request, 'accounts/signup.html')


def login(request):
	if request.method == 'POST':
		user = auth.authenticate(username = request.POST['username'],password = request.POST['password'])
		if user is not None:
			auth.login(request,user)
			valuenext= request.POST.get('next')
			if valuenext:
				return HttpResponseRedirect(request.POST.get('next'))
			else:
				return redirect('home')
		else:
			return render(request, 'accounts/login.html', {'error': 'Username or password is incorrect.'})
	else:
		return render(request, 'accounts/login.html')

def logout(request):
	if request.method == 'POST':
		auth.logout(request)
		return redirect('home')






