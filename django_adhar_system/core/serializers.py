
# from click import style
from curses import meta
from dataclasses import field
from rest_framework import serializers
from .models import *
# from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = '__all__'


class ManagerSignupSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True}
        }
# there are gone save
    def create(self, validated_data):
        print(validated_data)
        user = User(
            email=self.validated_data['email'],
            username= self.validated_data['username']
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords do not match.'})

        user.set_password(password)
        user.is_manager = True
        user.save()
        # Address.objects.create(user=user)
        return user




class StaffSignupSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True}
        }
# there are gone save
    def create(self, validated_data):
        print(validated_data)
        user = User(
            email=self.validated_data['email'],
            username= self.validated_data['username']
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords do not match.'})

        user.set_password(password)
        user.is_staff = True
        user.save()
        # Adhar.objects.create(user=user)
        return user

class AddressSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Address
        fields = ['street','city' , 'state' , 'postal_code','aadhar' ]



class AdharSerializer(serializers.ModelSerializer):
    address_f = AddressSerializer( many=True, read_only=True)

    class Meta:
        model = Aadhar
        fields = ['aadhar_number','is_active']


    def create(self, validated_data):
        aadhar_data = validated_data.pop('address_f')
        Addres = Address.objects.create(**validated_data)
    
        for track_data in aadhar_data:
            Aadhar.objects.create(Addres = Addres, **track_data)
        return Address

