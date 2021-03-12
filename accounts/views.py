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


def UserRegister(request):
	form = RegisterForm(request.POST or None)
	if form.is_valid():
		global cd, code
		cd = form.cleaned_data
		code = randint(10100, 30100)
		subject = 'Verify Code' ; msg = f"you code is {code} for {cd['email']} registration"
		send_mail(subject, msg, 'info@mega.ir', (cd['email'],))
		return redirect('accounts:verify')
	return render(request, 'accounts/register.html', {'form':form})

def VerifyCode(request):
	form = VerifyForm(request.POST or None)
	if form.is_valid():
		verifier = form.cleaned_data.get('verifier')
		if code == verifier:
			user = User.objects.create_user(email=cd['email'], password=cd['password1'])
			user.save()
			login(request, user)
			messages.success(request, 'شما با موفقیت ثبت نام کردید')
			return redirect('core:home')
		else:
			messages.error(request, 'کد وارد شده اشتباه است')
			return redirect('accounts:verify')
	return render(request, 'accounts/verify.html', {'form':form})


class UserLogin(AuthenticatedMixin, message, views.LoginView):
	template_name = 'accounts/login.html'
	success_message = 'ورود با موفقیت انجام شد'


class UserLogout(views.LogoutView):
	def get(self, request, *args, **kwargs):
		if not request.user.is_authenticated:
			return redirect('/')
		return super().get(request, *args, **kwargs)


class PasswordChange(message, views.PasswordChangeView):
	template_name = 'accounts/password_change_form.html'
	success_url = reverse_lazy('core:home')
	success_message = 'پسسورد شما با موفقیت عوض شد'
