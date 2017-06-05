from django import forms

class SignUpForm(forms.Form):
	username = forms.CharField()
	password1 = forms.CharField()
	password2 = forms.CharField()
	
	address = forms.CharField()

	def sign_up (self):
		from .models import MyUser

		if self.cleaned_data['password1'] == self.cleaned_data['password2']:
			return MyUser.objects.create(
				username = self.cleaned_data['username'],
				password = self.cleaned_data['password1'],
				address = self.cleaned_data['address']
			)

		else:
			return False

class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField()

	def login (self):
		from .models import MyUser

		user = MyUser.objects.filter(
			username=self.cleaned_data['username'],
			password=self.cleaned_data['password']
		)
		
		return user

class OrderForm (forms.Form):
	menu = forms.CharField()
	bread = forms.CharField()






