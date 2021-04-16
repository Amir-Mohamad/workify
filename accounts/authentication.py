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

# =========================================================

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


# FORMS.PY

# class RegisterForm(forms.ModelForm):
# 	class Meta:
# 		model = User
# 		fields = ('email', 'password1', 'password2')


# =========================================================

# NEW AUTH VIEW - EMAD

# class UserRegister(AuthenticatedMixin, message, CreateView):
# 	template_name = 'accounts/register.html'
# 	form_class = RegisterForm
# 	success_url = reverse_lazy('core:home')
# 	success_message = 'now, we send you a verify code, enter here.'

# 	def form_valid(self, form):
# 		valid = super().form_valid(form)
# 		cd = form.cleaned_data
# 		user = form.save(commit=False)
# 		user.set_password(cd['password1'])
# 		user.is_active = False
# 		user.save()
# 		global code, pk
# 		pk = user.id
# 		code = randint(10100, 30100)
# 		subject = 'Verify Code' ; msg = f"you code is {code} for {cd['email']} registration"
# 		send_mail(subject, msg, 'info@mega.ir', (cd['email'],))
# 		return redirect('accounts:verify')

# class VerifyCode(AuthenticatedMixin, FormView):
# 	template_name = 'accounts/verify.html'
# 	form_class = VerifyForm
# 	success_url = reverse_lazy('core:home')

# 	def form_valid(self, form):
# 		valid = super().form_valid(form)
# 		cd = form.cleaned_data
# 		if code == cd['verify_code']:
# 			user = get_object_or_404(User, pk=pk)
# 			user.is_active = True
# 			user.save()
# 			login(self.request, user)
# 			messages.success(self.request, 'you are registerd successfully and logged in.', 'success')
# 			return redirect(self.success_url)
# 		else:
# 			messages.error(self.request, 'code is wrong', 'danger')
# 			return redirect('accounts:verify')

# FORMS.PY

# class RegisterForm(forms.ModelForm):
# 	class Meta:
# 		model = User
# 		fields = ('email', 'password1', 'password2')
