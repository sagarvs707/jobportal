from django.core.validators import RegexValidator
from django.db import models


class AddCandidate(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,14}$', message="Phone number entered in the format:'+919999999999'. Up to 14 digits number")
    phone_number            = models.CharField(validators=[phone_regex], max_length=17, blank=True)  # validators should be a list
    alternate_phone_number  = models.CharField(validators=[phone_regex],max_length=17, blank=True)
    name                    = models.CharField(max_length=255, null=True, blank=True)
    sureame                 = models.CharField(max_length=255, null=True, blank=True)
    email                   = models.EmailField(max_length=255, unique=True)
    candidate_location      = models.CharField(max_length=512, null=True, blank=True)
    date_of_birth           = models.DateField(null=True, blank=True)
    gender                  = models.CharField(max_length=255, null=True, blank=True)
    job_interest            = models.CharField(max_length=512, null=True, blank=True)
    candidates_edu          = models.CharField(max_length=512, null=True, blank=True)
    college_name            = models.CharField(max_length=512, null=True, blank=True)
    name_of_degree          = models.CharField(max_length=512, null=True, blank=True)
    passing_year            = models.CharField(max_length=512, null=True, blank=True)
    candidate_experience    = models.CharField(max_length=512, null=True, blank=True)
    expected_salary         = models.CharField(max_length=512, null=True, blank=True)
    notice_period           = models.CharField(max_length=512, null=True, blank=True)
    candidate_job_role      = models.CharField(max_length=512, null=True, blank=True)
    languege_knows          = models.CharField(max_length=1024, null=True, blank=True)
    add_skills              = models.TextField(max_length=1024, null=True, blank=True)

    """notification"""
    sms_notification        = models.BooleanField(default=False)
    email_notification      = models.BooleanField(default=False)

    """ Valid and Invalid """
    valid                   = models.BooleanField(default=False)

    """session_id"""
    sessionid               = models.CharField(max_length=512, null=True, blank=True)

    """resume upload"""
    resume_upload           = models.FileField(upload_to='documents/', null=True, blank=True)


    def __str__(self):
        return self.name + "_" + self.sureame + "____" + str(self.id)

    def delete(self, *args, **kwargs):
        self.resume_upload.delete()
        super().delete(*args, **kwargs)

    @property
    def is_valid(self):
        return self.valid


