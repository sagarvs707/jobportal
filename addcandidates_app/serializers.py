from rest_framework import serializers
from addcandidates_app.models import AddCandidate


class AddCandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddCandidate
        fields = "__all__"
