# from django.contrib.auth.backends import ModelBackend
# from accounts.models import User

# class EmailBackend(ModelBackend):

# 	def authenticate(self, request, username=None, password=None, **kwargs):
# 		# email = kwargs.get('email')
# 		try:
# 			User.objects.get(email=username)
# 		except User.DoesNotExist:
# 			return None

# 	def get_user(self, user_id):
# 	    	try:
# 	        	return User.objects.get(pk=user_id)
# 	    	except User.DoesNotExist:
# 	        	return None


# OLD AUTH VIEW - EMAD

# class UserRegister(AuthenticatedMixin, message, CreateView):
# 	template_name = 'accounts/register.html'
# 	form_class = RegisterForm
# 	success_url = reverse_lazy('core:home')
# 	success_message = 'Register was successfully and you logged in.'

# 	def form_valid(self, form):
# 		valid = super().form_valid(form)
# 		cd = form.cleaned_data
# 		user = form.save(commit=False)
# 		user.set_password(cd['password1'])
# 		user.save()
# 		user = authenticate(self.request, email=cd['email'], password=cd['password1'])
# 		if user is not None:
# 			login(self.request, self.object)
# 		return valid


