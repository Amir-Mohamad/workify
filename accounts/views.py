from random import randint
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, FormView
from django.contrib.auth import views
from django.contrib.auth import login, logout
from django.contrib.messages.views import SuccessMessageMixin as message
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from accounts.mixins import AuthenticatedMixin
from accounts.models import User
from accounts.forms import RegisterForm, ProfileForm, VerifyForm
# Create your views here.


class Profile(LoginRequiredMixin, message, UpdateView):
	model = User
	template_name = 'accounts/profile.html'
	form_class = ProfileForm
	success_url = reverse_lazy('accounts:profile')
	success_message = 'your account updated.'

	def get_object(self):
		return User.objects.get(pk=self.request.user.pk)

	def get_form_kwargs(self):
		kwargs = super().get_form_kwargs()
		file = self.request.FILES.get('avatar')
		kwargs.update({'file': file})
		return kwargs


class UserRegister(AuthenticatedMixin, message, CreateView):
	template_name = 'accounts/register.html'
	form_class = RegisterForm
	success_url = reverse_lazy('core:home')
	success_message = 'now, we send you a verify code, enter here.'

	def form_valid(self, form):
		valid = super().form_valid(form)
		cd = form.cleaned_data
		user = form.save(commit=False)
		user.set_password(cd['password1'])
		user.is_active = False
		user.save()
		global code, pk
		pk = user.id
		code = randint(10100, 30100)
		subject = 'Verify Code' ; msg = f"you code is {code} for {cd['email']} registration"
		send_mail(subject, msg, 'info@mega.ir', (cd['email'],))
		return redirect('accounts:verify')

class VerifyCode(AuthenticatedMixin, FormView):
	template_name = 'accounts/verify.html'
	form_class = VerifyForm
	success_url = reverse_lazy('core:home')

	def form_valid(self, form):
		valid = super().form_valid(form)
		cd = form.cleaned_data
		if code == cd['verify_code']:
			user = get_object_or_404(User, pk=pk)
			user.is_active = True
			user.save()
			login(self.request, user)
			messages.success(self.request, 'you are registerd successfully and logged in.', 'success')
			return redirect(self.success_url)
		else:
			messages.error(self.request, 'code is wrong', 'danger')
			return redirect('accounts:verify')


class UserLogin(AuthenticatedMixin, message, views.LoginView):
	template_name = 'accounts/login.html'
	success_message = 'login was successfully.'


class UserLogout(views.LogoutView):
	def get(self, request, *args, **kwargs):
		if not request.user.is_authenticated:
			return redirect('/')
		return super().get(request, *args, **kwargs)


class PasswordChange(message, views.PasswordChangeView):
	template_name = 'accounts/password_change_form.html'
	success_url = reverse_lazy('core:home')
	success_message = 'your password changed successfully.'
