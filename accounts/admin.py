from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserAccount

# Register your models here.



admin.site.register(UserAccount, UserAdmin)