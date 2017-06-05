from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect

# logged_in = False

def index (request):
	logged_in = False
	if request.session.get('user_id'):
		logged_in = True

	return render (request, 'index.html', {'logged': logged_in})

def signup (request):
	from .models import MyUser
	from .form import SignUpForm

	# if request.session.get('user_id', None):
	# 	return HttpResponseRedirect('/index')

	if request.method == 'POST':
		form = SignUpForm(request.POST)

		if form.is_valid():
			user_created = form.sign_up()

			if not user_created:
				return render (request, 'signup.html', {'form': form, 'error': 'Confirm Password Failed!!!'})

			else:
				return HttpResponseRedirect('/login')

	else:
		form = SignUpForm()


	return render (request, 'signup.html', {'form': form})


def login(request):
	from .models import MyUser
	from .form import LoginForm

	# if request.session.get('user_id', None):
	# 	return HttpResponseRedirect('/index')

	if request.method == 'POST':
		# logged_in = True
		form = LoginForm(request.POST)

		if form.is_valid():
			result = form.login()

			if not result:
				return render (request, 'login.html', {'form': form, 'error': 'Login Failed'})

			else:
				request.session['user_id'] = result[0].id
				print(request.session['user_id'])

				return HttpResponseRedirect('/index')

	else:
		form = LoginForm()


	return render (request, 'login.html', {'form': form})


def logout(request):
	del request.session['user_id']

	return render (request, 'login.html')


def order (request):
	from .models import Type

	logged_in = False
	if request.session.get('user_id'):
		logged_in = True

	current_url = request.resolver_match.url_name
	# price = Type.filter()

	return render (request, 'order.html', {'logged': logged_in})

def custom (request):
	from .models import Order
	from .form import OrderForm

	logged_in = False
	if request.session.get('user_id'):
		logged_in = True

	if request.method == 'POST':
		form = OrderForm(request.POST)
		return render (request, 'custom.html', {'logged': logged_in})
	
	return render (request, 'custom.html', {'logged': logged_in})

def thank (request):

	logged_in = False
	if request.session.get('user_id'):
		logged_in = True

	return render (request, 'thankyou.html', {'logged': logged_in})


