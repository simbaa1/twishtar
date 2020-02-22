from django.contrib.auth.models import BaseUserManager
from django.utils.translation import ugettext_lazy as _

class UserManager(BaseUserManager):

    """
    Custom user manager where email is unique identifier for authentication
    """
    def create_user(self, username, email, password, **extra_fields):
        """ Create and save a user with a given email and password
         """
        if not email:
            raise ValueError('Email is required')
        if not username:
            raise ValueError('Username is required.')

        email = self.normalize_email(email)
        user = self.model(username=username, email=email)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        if not password:
            raise ValueError(_('A password is required'))
        user=self.create_user(username, email, password, **extra_fields)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user
