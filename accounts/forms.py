from django import forms
from django.core.files.images import get_image_dimensions
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
# from PIL import Image
from accounts.models import User

class RegisterForm(forms.Form):
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))


class VerifyForm(forms.Form):
    verifier = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))


class ProfileForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		self.file = kwargs.pop('file')
		super().__init__(*args, **kwargs)

	class Meta:
		model = User
		fields = ("email", "first_name", "last_name", "avatar")
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
