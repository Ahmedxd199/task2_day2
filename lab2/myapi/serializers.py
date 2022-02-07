from rest_framework import serializers

from Home.models import Register


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model=Register
        fields = '__all__'
