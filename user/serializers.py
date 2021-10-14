from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from .models import User
from django.db import transaction




class CustomRegisterSerializer(RegisterSerializer):
    full_name = serializers.CharField()

    def get_cleaned_data(self):
        super(CustomRegisterSerializer,self).get_cleaned_data()
        return{
            'full_name': self.validated_data.get('full_name',''),
            'username': self.validated_data.get('username',''),
            'email': self.validated_data.get('email',''),
            'password1': self.validated_data.get('password1',''),
            'password2': self.validated_data.get('password2',''),
        }



