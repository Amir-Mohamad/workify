from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import User

class RegisterForm(UserCreationForm):
	class Meta:
		model = User
		fields = ('email', 'password1', 'password2')


class ProfileForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

	class Meta:
		model = User
		fields = ("email", "first_name", "last_name", "avatar")