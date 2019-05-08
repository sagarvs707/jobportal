from django.core.validators import RegexValidator
from django.db import models

# Create your models here.
class AddUsers(models.Model):
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,14}$', message="Phone number entered in the format:'+919999999999'. Up to 14 digits number")
    mobile_number = models.CharField(validators=[phone_regex], unique=True, max_length=14, blank=True)  # validators should be a listphone_regex = RegexValidator(regex=r'^\+?1?\d{9,14}$', message="Phone number entered in the format:'+919999999999'. Up to 14 digits number")
    password = models.CharField(max_length=124)
    """Permission for users"""
    create_applications = models.BooleanField(default=False, blank=True)
    # view_account_information = models.BooleanField()
    # see_commercials = models.BooleanField()
    # secondery_manager_permissions = models.BooleanField()
    # deactivate_manager_permissions = models.BooleanField()