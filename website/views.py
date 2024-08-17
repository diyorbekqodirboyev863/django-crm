from django.contrib import messages as msg
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

# Index.
def index(request):
	'''Home page.'''
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		# Authenticate.
		user = authenticate(request=request, username=username, password=password)
		if user is not None:
			login(request=request, user=user)
			msg.success(request=request, message=(f'Hi {user.username}!'))
			return redirect(to='index')
		else:
			msg.warning(request=request, message=('Please repeat these actions again!'))
			return redirect(to='index')
	else:
		return render(request=request, template_name='index.html', context={})

# Logout.
def logout_user(request):
	'''Logout.'''
	logout(request)
	msg.info(request=request, message=('You are logged out.'))
	return redirect(to='index')

# Register.
def register_user(request):
	return render(request=request, template_name='register.html', context={})