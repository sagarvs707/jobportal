from rest_framework import serializers
from addcandidates_app.models import AddCandidate


class AddCandidateSerializer(serializers.ModelSerializer):
    resume_upload = serializers.FileField(use_url=True)

    class Meta:
        model = AddCandidate
        fields = ('id', 'phone_number', 'alternate_phone_number', 'name', 'sureame', 'email', 'candidate_location',
                  'date_of_birth', 'gender', 'job_interest', 'candidates_edu', 'college_name', 'name_of_degree',
                  'passing_year', 'candidate_experience', 'expected_salary', 'notice_period', 'candidate_job_role',
                  'languege_knows', 'add_skills', 'sms_notification', 'email_notification', 'valid', 'resume_upload')
