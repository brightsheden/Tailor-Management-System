from django.db.models import fields
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *
from rest_framework_simplejwt.tokens import RefreshToken


class UserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(read_only=True)
    _id = serializers.SerializerMethodField(read_only=True)
    isAdmin = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User 
        fields = ['id',"_id",'username','name', 'email',"isAdmin",]

    def get_name(self,obj):
        name= obj.first_name
        if name == "":
            name = obj.email
        return name

    def get__id(self,obj):
        return obj.id
    
    def get_isAdmin(self,obj):
        return obj.is_staff

class UserSerializerWithToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        fields = ['id', 'username','email',"isAdmin",'name', 'token']

    def get_token(self, obj):
        token =RefreshToken.for_user(obj)
        return str(token.access_token)



class ProfileSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Profile
        fields = "__all__"


class FashionCompanySerializer(serializers.ModelSerializer):
   
    class Meta:
        model = FashionCompany
        fields = "__all__"

class TailorSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Tailor
        fields = "__all__"


class CustomerSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Customer
        fields = "__all__"



class StyleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Style
        fields = "__all__"


class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work
        fields = "__all__"




  