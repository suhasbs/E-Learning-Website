from django import forms
from django.contrib.auth.models import User

# class UserForm(forms.ModelForm):
# 	password = forms.CharField(widget=forms.PasswordInput) 

# 	class Meta:
# 		model = User
# 		fields = ['username', 'email', 'password', 'first_name', 'last_name']
		# fields = "__all__"

class UserLoginForm(forms.Form):
	username = forms.CharField(max_length=150)
	password = forms.CharField(widget=forms.PasswordInput) 