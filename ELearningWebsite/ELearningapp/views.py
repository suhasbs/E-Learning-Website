# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse
from django.views import View
from .forms import UserLoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
# Create your views here.

def index(request):
	return HttpResponse("Index")


class LoginView(View):
	form_class = UserLoginForm
	template_name = 'ELearningapp/login.html'

	def get(self, request):
		if request.user.is_authenticated():
			return redirect("ELearningapp:index")
		form = self.form_class(None)
		return render(request, self.template_name, {'form':form})

	def post(self, request):
		form = self.form_class(request.POST)
		print form
		if form.is_valid():
			# user = form.save(commit=False)
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			# user.set_password(password)
			# user.save()
			# print "User created"
			user = authenticate(username=username, password=password)
			if user is not None:
				if user.is_active:
					login(request, user)
					if(request.GET.get('next')):
						print "Here"
						return redirect(request.GET['next'])
					return redirect('ecom_webapp:index')
			else:
				error_msg = "Wrong Login Credentials! "
				return render(request, "ELearningapp/login.html", {'error_msg': error_msg})