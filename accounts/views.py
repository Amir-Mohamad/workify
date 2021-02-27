from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import authenticate, login, logout
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from accounts.models import User
from accounts.forms import RegisterForm
# Create your views here.


class UserRegister(CreateView):
	template_name = 'accounts/register.html'
	form_class = RegisterForm

	def get(self, request, *args, **kwargs):
		if request.user.is_authenticated:
			return redirect('/')
		return super().get(request, *args, **kwargs)

	def form_valid(self, form):
		valid = super().form_valid(form)
		cd = form.cleaned_data
		user = form.save(commit=False)
		user.set_password(cd['password1'])
		user.save()
		user = authenticate(self.request, email=cd['email'], password=cd['password1'])
		if user is not None:
			login(self.request, self.object)
		return valid

	def get_success_url(self):
		messages.success(self.request, 'Register was successfully and you logged in.')
		return reverse_lazy('core:home')


class UserLogin(LoginView):
	template_name = 'accounts/login.html'

	def get(self, request, *args, **kwargs):
		if request.user.is_authenticated:
			return redirect('/')
		return super().get(request, *args, **kwargs)

	def get_success_url(self):
		messages.success(self.request, 'login was successfully.')
		return reverse_lazy('core:home')


@login_required
def UserLogout(request):
    logout(request)
    messages.success(request, 'logout was successfully.')
    return redirect('core:home')


# class UserLogout(SuccessMessageMixin, LogoutView):
# 	success_message = 'logout was successfully.'
