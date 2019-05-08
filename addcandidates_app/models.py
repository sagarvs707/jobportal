import os

from django.core.validators import RegexValidator
from django.db import models


class It_Jobs(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,14}$', message="Phone number entered in the format:'+919999999999'. Up to 14 digits number")
    phone_number            = models.CharField(validators=[phone_regex], max_length=17, blank=True)  # validators should be a list
    alternate_phone_number  = models.CharField(validators=[phone_regex],max_length=17, blank=True)
    name                    = models.CharField(max_length=255, null=True, blank=True)
    sureame                 = models.CharField(max_length=255, null=True, blank=True)
    email                   = models.EmailField(max_length=255, unique=True)
    candidate_location      = models.CharField(max_length=512, null=True, blank=True)
    date_of_birth           = models.DateField(null=True, blank=True)
    gender                  = models.CharField(max_length=255, null=True, blank=True)

    candidates_edu          = models.CharField(max_length=512, null=True, blank=True)
    tenth_passing           = models.CharField(max_length=512, null=True, blank=True)

    puc_passing             = models.CharField(max_length=512, null=True, blank=True)
    strem                   = models.CharField(max_length=512, null=True, blank=True)

    graduation_college_name         = models.CharField(max_length=512, null=True, blank=True)
    graduation_name_of_degree       = models.CharField(max_length=512, null=True, blank=True)
    graduation_passing_year         = models.CharField(max_length=512, null=True, blank=True)

    post_graduation_college_name    = models.CharField(max_length=512, null=True, blank=True)
    post_graduation_name_of_degree  = models.CharField(max_length=512, null=True, blank=True)
    post_graduation_passing_year    = models.CharField(max_length=512, null=True, blank=True)

    candidate_experience            = models.CharField(max_length=512, null=True, blank=True)

    fresher_expected_salary_package = models.CharField(max_length=512, null=True, blank=True)
    fresher_expected_salary         = models.CharField(max_length=512, null=True, blank=True)

    current_salary_package          = models.CharField(max_length=512, null=True, blank=True)
    current_salary                  = models.CharField(max_length=512, null=True, blank=True)
    expected_salary_package         = models.CharField(max_length=512, null=True, blank=True)
    expected_salary                 = models.CharField(max_length=512, null=True, blank=True)
    work_experience_of_year         = models.CharField(max_length=512, null=True, blank=True)
    work_experience_of_month        = models.CharField(max_length=512, null=True, blank=True)

    candidate_job_role      = models.CharField(max_length=512, null=True, blank=True)
    languege_can_speak_well = models.CharField(max_length=1024, null=True, blank=True)
    add_skills              = models.TextField(max_length=1024, null=True, blank=True)

    """notification"""
    sms_notification        = models.BooleanField(default=False)
    email_notification      = models.BooleanField(default=False)
    send_otp                = models.BooleanField(default=False)

    """ Valid and Invalid """
    valid                   = models.BooleanField(default=False)

    """session_id"""
    sessionid               = models.CharField(max_length=512, null=True, blank=True)

    """resume upload"""
    resume_upload           = models.FileField(blank=True)


    def __str__(self):
        return self.name + "_" + self.sureame + "____" + str(self.id)

    def delete(self, *args, **kwargs):
        if os.path.isfile(self.resume_upload.path):
            os.remove(self.resume_upload.path)

        super(It_Jobs, self).delete(*args, **kwargs)

    @property
    def is_valid(self):
        return self.valid



class Non_It_Jobs(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,14}$', message="Phone number entered in the format:'+919999999999'. Up to 14 digits number")
    phone_number            = models.CharField(validators=[phone_regex], max_length=17, blank=True)  # validators should be a list
    alternate_phone_number  = models.CharField(validators=[phone_regex],max_length=17, blank=True)
    name                    = models.CharField(max_length=255, null=True, blank=True)
    sureame                 = models.CharField(max_length=255, null=True, blank=True)
    email                   = models.EmailField(max_length=255, unique=True)
    candidate_location      = models.CharField(max_length=512, null=True, blank=True)
    date_of_birth           = models.DateField(null=True, blank=True)
    gender                  = models.CharField(max_length=255, null=True, blank=True)

    candidates_edu          = models.CharField(max_length=512, null=True, blank=True)

    tenth_passing           = models.CharField(max_length=512, null=True, blank=True)

    puc_passing             = models.CharField(max_length=512, null=True, blank=True)
    strem                   = models.CharField(max_length=512, null=True, blank=True)

    graduation_college_name         = models.CharField(max_length=512, null=True, blank=True)
    graduation_name_of_degree       = models.CharField(max_length=512, null=True, blank=True)
    graduation_passing_year         = models.CharField(max_length=512, null=True, blank=True)

    post_graduation_college_name    = models.CharField(max_length=512, null=True, blank=True)
    post_graduation_name_of_degree  = models.CharField(max_length=512, null=True, blank=True)
    post_graduation_passing_year    = models.CharField(max_length=512, null=True, blank=True)

    candidate_experience            = models.CharField(max_length=512, null=True, blank=True)

    fresher_expected_salary_package = models.CharField(max_length=512, null=True, blank=True)
    fresher_expected_salary         = models.CharField(max_length=512, null=True, blank=True)

    current_salary_package          = models.CharField(max_length=512, null=True, blank=True)
    current_salary                  = models.CharField(max_length=512, null=True, blank=True)
    expected_salary_package         = models.CharField(max_length=512, null=True, blank=True)
    expected_salary                 = models.CharField(max_length=512, null=True, blank=True)
    work_experience_of_year         = models.CharField(max_length=512, null=True, blank=True)
    work_experience_of_month        = models.CharField(max_length=512, null=True, blank=True)

    languege_can_speak_well         = models.CharField(max_length=1024, null=True, blank=True)

    """notification"""
    sms_notification        = models.BooleanField(default=False)
    email_notification      = models.BooleanField(default=False)
    send_otp                = models.BooleanField(default=False)


    """ Valid and Invalid """
    valid                   = models.BooleanField(default=False)

    """session_id"""
    sessionid               = models.CharField(max_length=512, null=True, blank=True)

    """resume upload"""
    resume_upload           = models.FileField(blank=True)


    def __str__(self):
        return self.name + "_" + self.sureame + "____" + str(self.id)

    def delete(self, *args, **kwargs):
        if os.path.isfile(self.resume_upload.path):
            os.remove(self.resume_upload.path)

        super(Non_It_Jobs, self).delete(*args, **kwargs)

    @property
    def is_valid(self):
        return self.valid



class Delivery_Boy(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,14}$', message="Phone number entered in the format:'+919999999999'. Up to 14 digits number")
    phone_number            = models.CharField(validators=[phone_regex], max_length=17, blank=True)  # validators should be a list
    alternate_phone_number  = models.CharField(validators=[phone_regex],max_length=17, blank=True)
    name                    = models.CharField(max_length=255, null=True, blank=True)
    sureame                 = models.CharField(max_length=255, null=True, blank=True)

    android_phone           = models.BooleanField(default=False)

    candidate_location      = models.CharField(max_length=512, null=True, blank=True)
    date_of_birth           = models.DateField(null=True, blank=True)
    gender                  = models.CharField(max_length=255, null=True, blank=True)

    candidate_experience            = models.CharField(max_length=512, null=True, blank=True)

    fresher_expected_salary_package = models.CharField(max_length=512, null=True, blank=True)
    fresher_expected_salary         = models.CharField(max_length=512, null=True, blank=True)

    current_salary_package          = models.CharField(max_length=512, null=True, blank=True)
    current_salary                  = models.CharField(max_length=512, null=True, blank=True)
    expected_salary_package         = models.CharField(max_length=512, null=True, blank=True)
    expected_salary                 = models.CharField(max_length=512, null=True, blank=True)
    work_experience_of_year         = models.CharField(max_length=512, null=True, blank=True)
    work_experience_of_month        = models.CharField(max_length=512, null=True, blank=True)

    do_you_have_bike            = models.BooleanField(default=False)
    do_you_have_driving_licence = models.BooleanField(default=False)

    languege_can_speak_well         = models.CharField(max_length=1024, null=True, blank=True)

    """notification"""
    sms_notification        = models.BooleanField(default=False)
    send_otp                = models.BooleanField(default=False)

    # email_notification      = models.BooleanField(default=False)

    """ Valid and Invalid """
    valid                   = models.BooleanField(default=False)

    """session_id"""
    sessionid               = models.CharField(max_length=512, null=True, blank=True)

    """resume upload"""
    resume_upload           = models.FileField(blank=True)


    def __str__(self):
        return self.name+"_"+self.sureame + "____" + str(self.id)

    def delete(self, *args, **kwargs):
        if os.path.isfile(self.resume_upload.path):
            os.remove(self.resume_upload.path)

        super(Delivery_Boy, self).delete(*args, **kwargs)

    @property
    def is_valid(self):
        return self.valid
