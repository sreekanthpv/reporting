from rest_framework import serializers
from reporting.models import MyUser,Course,Batch
from rest_framework.serializers import ModelSerializer


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ["email","role","password"]
    def create(self, validated_data):
        return MyUser.objects.create_user(email=validated_data["email"],
                                          password=validated_data["password"],
                                          role=validated_data["role"])


class LoginSerializer(serializers.Serializer):
      email = serializers.EmailField()
      password = serializers.CharField()

class AddCourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = ["course_name"]

class AddBatchSerializer(ModelSerializer):
    class Meta:
        model = Batch
        fields = ["course","batch_name"]

