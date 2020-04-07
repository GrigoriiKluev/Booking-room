from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, get_user_model,login, logout
from AuthApp.forms import UserLoginForm, UserRegisterForm



def login_view(request):
	#next_after = request.GET.get('next')
	form = UserLoginForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data.get('username')
		password = form.cleaned_data.get('password')
		user = authenticate(username = username, password=password)
		login(request, user)
		#if next_after:
			#return redirect (next_after)
		return redirect ('/info')
	context = {
		'form':form,

	}
	return render (request, 'authapp/login.html', context )



def register_view(request):
	next_after = request.GET.get('next')
	form = UserRegisterForm(request.POST or None)
	if form.is_valid():
		user = form.save(commit = False)
		password = form.cleaned_data.get('password')
		user.set_password(password)
		user.save()
		new_user = authenticate(username= user.username, password = password)
		login(request, new_user)
		return redirect('/info')
	context = {
		'form':form,

	}
	return render (request, 'authapp/signup.html', context )

def logout_view(request):
	logout(request)
	return redirect('/info')
