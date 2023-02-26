from rest_framework import serializers
from app_jwt1.models import User

class UserRegistionViewSerialzer(serializers.ModelSerializer):
    password2=serializers.CharField(style={'input_type':'password'},write_only=True)
    class Meta:
        model=User
        fields=['email','name','date_of_birth','password','password2']
        extra_kwargs={
            'password2':{'write_only':True}
        }
    def create(self, validate_data):
        return User.objects.create_user(**validate_data)
    def validate(self,data):
        password=data.get('password')
        password2=data.get('password2')
        if password!=password2:
            raise serializers.ValidationError('Password and password2 dont match')
        return data
class UserLoginViewSerialzer(serializers.ModelSerializer):
    email=serializers.EmailField(max_length=255)
    class Meta:
        model=User
        fields=['email','password']