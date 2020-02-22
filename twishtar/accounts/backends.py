from django.conf import settings


class EmailAuthBackend(object):

    """
    Allow authentication using email
    """
    def authenticate(self, request, username=None, password=None):
        try:
            user = settings.AUTH_USER_MODEL.objects.get(email=username)
            if user.check_password(password):
                return User
            return None
        
        except settings.AUTH_USER_MODEL.DoesNotExist:
            return None

    
    def get_user(self, user_id):
        try:
            return settings.AUTH_USER_MODEL.objects.get(pk=user_id)
        except settings.AUTH_USER_MODEL.DoesNotExist:
            return None