from rest_framework import serializers
from addusers.models import AddUsers


class AddusersSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddUsers
        fields = ('id', 'first_name', 'last_name', 'email', 'mobile_number', 'password', 'create_applications')