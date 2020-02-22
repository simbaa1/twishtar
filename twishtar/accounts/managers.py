from django.contrib.auth.base_use import BaseUserManager
from django.utils.translation import ugettext_lazy as _

class CustomManager(BaseUserManager):

    """
    Custom user manager where email is unique identifier for authentication
    """
    def create_user(self, username, email, password, **extra_fields):
        """ Create and save a user with a given email and password
         """
        pass
