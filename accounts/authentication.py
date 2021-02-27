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
