# from django.utils import timezone
from datetime import datetime

from django.conf import settings
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class UserManager(BaseUserManager):
   def _create_user(self, username, email, password, is_active, is_staff, is_superuser, **extra_fields):
      now = datetime.now()
      
      if not username:
         raise ValueError("The given username is not valid")
      email = self.normalize_email(email)
      user = self.model(
         username=username,
         email=email,
         is_active=is_active,
         is_staff=is_staff,
         is_superuser=is_superuser,
         date_joined=now,
         **extra_fields
      )
      user.set_password(password)
      user.save(using=self._db)
      return user
   
   def create_user(self, username, email, password, **extra_fields):
      return self._create_user(
         username,
         email,
         password,
         is_active=True,
         is_staff=True,
         is_superuser=False,
         **extra_fields
      )
   
   def create_superuser(self, username, email, password, **extra_fields):
      user = self._create_user(
         username,
         email,
         password,
         is_active=True,
         is_staff=True,
         is_superuser=True,
         **extra_fields
      )
      user.save(using=self._db)
      return user


class User(AbstractBaseUser, PermissionsMixin):
   staff_id = models.CharField(unique=True, null=False, max_length=4)
   username = models.CharField(max_length=30, unique=True)
   email = models.EmailField(max_length=250, unique=True)
   first_name = models.CharField(max_length=30, blank=True, null=True)
   last_name = models.CharField(max_length=30, blank=True, null=True)
   first_name_kh = models.CharField(max_length=30, blank=True, null=True)
   last_name_kh = models.CharField(max_length=30, blank=True, null=True)
   
   GENDER_CHOICES = (
      ('M', 'Male'),
      ('F', 'Female'),
      ('O', 'Others')
   )
   gender = models.CharField(choices=GENDER_CHOICES, max_length=1, default=None, null=True)
   # date_of_birth = models.DateTimeField(blank=True, null=True)
   address = models.CharField(max_length=250, blank=True, null=True)
   # profile_image = models.ImageField(null=True)
   phone_number = models.CharField(max_length=25, null=True, blank=True)
   ext = models.CharField(max_length=25, null=True, blank=True)
   
   is_active = models.BooleanField(default=True)
   is_staff = models.BooleanField(default=False)
   is_superuser = models.BooleanField(default=False)
   date_joined = models.DateTimeField(default=datetime.now())
   
   objects = UserManager()
   USERNAME_FIELD = 'username'
   REQUIRED_FIELDS = ['email', ]
   
   @property
   def fullname(self):
      return f'{self.last_name} {self.first_name}'


# Auto create user auth token when user created
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def GenerateToken(sender, instance=None, created=False, **kwargs):
   if created:
      Token.objects.create(user=instance)
