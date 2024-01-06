from rest_framework import serializers
from .models import UserModel

class UserSerializer(serializers.ModelSerializer):

    def __init__(self, *args, **kwargs):
        super(UserSerializer, self).__init__(*args, **kwargs)
        if self.context['request'].method == "PUT":
            self.fields.pop('password')

    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = UserModel
        exclude = ["groups", "user_permissions", "last_login"]

    def create(self, validated_data):
        user: UserModel = super().create(validated_data)
        user.set_password(validated_data.get("password"))
        user.save()
        return user