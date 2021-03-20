from django import forms
from django.core.files.images import get_image_dimensions
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from django.core.validators import EmailValidator
from accounts.models import User


messages = {
	'required':'این فیلد اجباری است',
	'invalid':'لطفا یک ایمیل معتبر وارد کنید',
	'max_length':'تعداد کاراکترها بیشتر از حد مجاز است'
}


class RegisterForm(forms.Form):
	email = forms.EmailField(
		widget=forms.EmailInput(attrs={'class':'form-control'}),
		label='email',
		validators=[EmailValidator('correct email'),],
		error_messages=messages,
	)
	password1 = forms.CharField(error_messages=messages,widget=forms.PasswordInput(attrs={'class':'form-control'}))
	password2 = forms.CharField(error_messages=messages, widget=forms.PasswordInput(attrs={'class':'form-control'}))

	def clean_email(self):
		email = self.cleaned_data.get('email')
		is_exists = User.objects.filter(email=email).exists()
		if is_exists:
			raise forms.ValidationError('Already exists.')
		return email

	def clean_password2(self):
		password1 = self.cleaned_data.get('password1')
		password2 = self.cleaned_data.get('password2')
		if password1 != password2:
			raise forms.ValidationError('don\'t match.')
		if len(password2) < 8:
		    raise forms.ValidationError('8 chars.')
		return password2


class VerifyForm(forms.Form):
    verifier = forms.IntegerField(error_messages=messages)


class ProfileForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		self.file = kwargs.pop('file')
		super().__init__(*args, **kwargs)

	class Meta:
		model = User
		fields = ("email", "first_name", "last_name", "avatar", "team_member")
		widgets = {'avatar':forms.FileInput}

	def clean_avatar(self):
		if self.file is not None:
			picture = self.cleaned_data.get('avatar')
			if picture is None: return picture
			width, height = get_image_dimensions(picture)
			content_type = picture.content_type.split('/')
			# im = Image.open(picture)
			# im = im.size - > picture width, height
			if content_type[0] in settings.CONTENT_TYPES and content_type[1] in settings.VALID_FORMATS:
				if picture.size > settings.MAX_UPLOAD_SIZE:
					raise forms.ValidationError('Please keep filesize under 2 MB')
			else:
				raise forms.ValidationError('File type is not supported')

			return picture
		return
		# if width != 200:
		# 	raise forms.ValidationError("The image is %i pixel wide. It's supposed to be 100px" % width)
		# if height != 200:
		# 	raise forms.ValidationError("The image is %i pixel high. It's supposed to be 200px" % height)
	
		# return picture
