from django import forms
from django.core.files.images import get_image_dimensions
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
# from PIL import Image
from accounts.models import User

class RegisterForm(UserCreationForm):
	class Meta:
		model = User
		fields = ('email', 'password1', 'password2')


class ProfileForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		# self.fields['avatar'].validators = []

	class Meta:
		model = User
		fields = ("email", "first_name", "last_name", "avatar")
		# widgets = {'avatar':forms.FileInput}

	def clean_avatar(self):
		picture = self.cleaned_data['avatar']
		width, height = get_image_dimensions(picture)
		content_type = picture.content_type.split('/')
		# im = Image.open(picture)
		# im = im.size # - > picture width, height
		if content_type[0] in settings.CONTENT_TYPES and content_type[1] in settings.VALID_FORMATS:
			if picture.size > settings.MAX_UPLOAD_SIZE:
				raise forms.ValidationError('Please keep filesize under 2 MB')
		else:
			raise forms.ValidationError('File type is not supported')
		return picture



		# if width != 200:
		# 	raise forms.ValidationError("The image is %i pixel wide. It's supposed to be 100px" % width)
		# if height != 200:
		# 	raise forms.ValidationError("The image is %i pixel high. It's supposed to be 200px" % height)
	
		# return picture