from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from django.contrib.auth import views
from django.contrib.auth import authenticate, login, logout
from django.contrib.messages.views import SuccessMessageMixin as message
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from accounts.models import User
from accounts.forms import RegisterForm, ProfileForm
# Create your views here.


class Profile(LoginRequiredMixin, message, UpdateView):
	model = User
	template_name = 'accounts/profile.html'
	form_class = ProfileForm
	success_url = reverse_lazy('accounts:profile')
	success_message = 'your account updated.'

	def get_object(self):
		return User.objects.get(pk=self.request.user.pk)


class UserRegister(message, CreateView):
	template_name = 'accounts/register.html'
	form_class = RegisterForm
	success_url = reverse_lazy('core:home')
	success_message = 'Register was successfully and you logged in.'

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


class UserLogin(message, views.LoginView):
	template_name = 'accounts/login.html'
	success_message = 'login was successfully.'

	def get(self, request, *args, **kwargs):
		if request.user.is_authenticated:
			return redirect('/')
		return super().get(request, *args, **kwargs)


@login_required
def UserLogout(request):
    logout(request)
    messages.success(request, 'logout was successfully.')
    return redirect('core:home')


# Password Change
class psschng(message, views.PasswordChangeView):
	template_name = 'accounts/password_change_form.html'
	success_url = reverse_lazy('core:home')
	success_message = 'your password changed successfully.'
