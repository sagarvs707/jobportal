from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager
)
# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email,  password=None, full_name=None, address=None, phone_number=None, is_active=True, is_satff=False, is_admin=False):
        if not email:
            raise ValueError("user must have an Email address")
        if not password:
            raise ValueError("user must have a password")
        if not phone_number:
            raise ValueError("user must have a phone number")

        user_obj = self.model(
            email=self.normalize_email(email),
            full_name=full_name,
            phone_number=phone_number,
            address=address
        )
        user_obj.set_password(password) #change user password
        user_obj.staff = is_satff
        user_obj.admin = is_admin
        user_obj.active = is_active

        user_obj.save(using=self._db)
        return user_obj

    def crete_staffuser(self, email, phone_number=None, password=None, full_name=None, address=None,):
        user = self.create_user(
            email,
            phone_number=phone_number,
            full_name=full_name,
            address=address,
            password=password,
            is_satff=True
        )
        return user

    def create_superuser(self, email, password=None, phone_number=None, full_name=None, address=None,):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            phone_number=phone_number,
            password=password,
            full_name=full_name,
            address=address,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email           = models.EmailField(max_length=255, unique=True)
    full_name       = models.CharField(max_length=255, null=True, blank=True)
    address         = models.CharField(max_length=255, null=True, blank=True)
    phone_regex     = RegexValidator(regex=r'^\+?1?\d{9,14}$',
                                 message="Phone number entered in the format:'+919999999999'. Up to 14 digits number")
    phone_number    = models.CharField(validators=[phone_regex], max_length=17, blank=True)  # validators should be a list

    active          = models.BooleanField(default=True)
    staff           = models.BooleanField(default=False)
    admin           = models.BooleanField(default=False)
    timestamp       = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email' # user name

    REQUIRED_FIELDS = ['phone_number', 'full_name', 'address']

    object = UserManager()

    def __str__(self):
         return self.email

    def get_full_name(self):
         return self.full_name

    def get_short_name(self):
         return self.full_name

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active