from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import mixins,generics,views,status
from rest_framework.response import Response
from reporting.models import MyUser,Course,Batch
from reportapi.serializers import RegistrationSerializer,LoginSerializer,AddCourseSerializer,AddBatchSerializer
from django.contrib.auth import authenticate,login,logout
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from rest_framework.authentication import BasicAuthentication,SessionAuthentication,TokenAuthentication
from rest_framework.authtoken.models import Token



class RegistrationView(mixins.CreateModelMixin,generics.GenericAPIView):
    model = MyUser
    serializer_class = RegistrationSerializer

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)


class SignInView(APIView):
    serializer_class = LoginSerializer

    def post(self,request,*args,**kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data["email"]
            print(email)
            password = serializer.validated_data["password"]
            print(password)
            user=authenticate(request,email=email,password=password)
            print(user)
            if user:
                login(request,user)
                token,created=Token.objects.get_or_create(user=user)
                return Response({"token":token.key},status=status.HTTP_200_OK)
                # return Response({"msg":"login succesfull"},status=status.HTTP_200_OK)
            else:
                return Response({"msg": "loginfailed"}, status=status.HTTP_400_BAD_REQUEST)

        else:
            return Response(serializer.errors)


class CourseView(generics.GenericAPIView,mixins.CreateModelMixin,mixins.ListModelMixin):
    model = Course
    serializer_class = AddCourseSerializer
    authentication_classes = [BasicAuthentication,TokenAuthentication]
    permission_classes = [IsAdminUser,IsAuthenticated]
    queryset = model.objects.all()

    def post(self,request,*args,**kwargs):
        if request.user.is_admin:
            return self.create(request,*args,**kwargs)
        else:
            return Response({"msg":"user must be admin"},status=status.HTTP_400_BAD_REQUEST)

    def get(self,request,*args,**kwargs):
        if request.user.is_admin:
            return self.list(request,*args,**kwargs)
        else:
            return Response({"msg": "user must be admin"}, status=status.HTTP_400_BAD_REQUEST)

class BatchView(generics.GenericAPIView,mixins.CreateModelMixin,mixins.ListModelMixin):
    model = Batch
    serializer_class = AddBatchSerializer
    authentication_classes = [BasicAuthentication,TokenAuthentication]
    permission_classes = [IsAdminUser]
    queryset = model.objects.all()

    def post(self,request,*args,**kwargs):
        if request.user.is_admin:
            return self.create(request,*args,**kwargs)
        else:
            return Response({"msg":"user must be admin"}, status=status.HTTP_400_BAD_REQUEST)
    def get(self,request,*args,**kwargs):
        if request.user.is_admin:
            return self.list(request, *args, **kwargs)
        else:
            return Response({"msg": "user must be admin"}, status=status.HTTP_400_BAD_REQUEST)




