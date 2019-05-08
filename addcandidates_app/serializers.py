from rest_framework import serializers
from addcandidates_app.models import It_Jobs, Non_It_Jobs, Delivery_Boy


class It_JobsSerializer(serializers.ModelSerializer):
    resume_upload = serializers.FileField(use_url=True)

    class Meta:
        model = It_Jobs
        fields = '__all__'

class Non_It_JobsSerializer(serializers.ModelSerializer):
    resume_upload = serializers.FileField(use_url=True)

    class Meta:
        model = Non_It_Jobs
        fields = '__all__'


class Delivery_BoySerializer(serializers.ModelSerializer):
    resume_upload = serializers.FileField(use_url=True)

    class Meta:
        model = Delivery_Boy
        fields = '__all__'


# fields = ('id', 'phone_number', 'alternate_phone_number', 'name', 'sureame', 'email', 'candidate_location',
#           'date_of_birth', 'gender', 'candidates_edu', 'tenth_passing', 'puc_passing', 'strem',
#           'graduation_college_name', 'graduation_name_of_degree', 'graduation_passing_year',
#           'post_graduation_college_name', 'post_graduation_name_of_degree',
#           'post_graduation_passing_year', 'candidate_experience', 'fresher_expected_salary_package',
#           'fresher_expected_salary',
#           'candidate_job_role',
#           'languege_knows', 'add_skills', 'sms_notification', 'email_notification', 'valid', 'resume_upload')
