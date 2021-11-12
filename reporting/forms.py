from django.forms import ModelForm
from reporting.admin import UserCreationForm
from reporting.models import MyUser,Course,Batch,TimeSheet
from django import forms
from datetime import datetime


class UserAddForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"})),
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"})),

    class Meta:
        model=MyUser
        fields=["email","role"]
        widgets={
            "email":forms.TextInput(attrs={"class":"form-control"}),
            "role": forms.Select(attrs={"class": "form-select"}),

        }

class CourseAddForm(forms.ModelForm):
    class Meta:
        model=Course
        fields=["course_name"]
        widgets = {
            "course_name": forms.TextInput(attrs={"class": "form-control"}),

        }


class BatchAddForm(forms.ModelForm):
    class Meta:
        model=Batch
        fields=["course","batch_name"]

        widgets = {
            "course": forms.Select(attrs={"class": "form-select"}),
            "batch_name": forms.TextInput(attrs={"class": "form-control"}),

        }

class UserLoginForm(forms.Form):
    email=forms.CharField(widget=(forms.EmailInput(attrs={"class":"form-control"})))
    password=forms.CharField(widget=(forms.PasswordInput(attrs={"class":"form-control"})))


class AddTimeSheetForm(forms.ModelForm):

    def __init__(self,user,*args,**kwargs):
        self.user=user
        super().__init__(*args,**kwargs)


    class Meta:
        model=TimeSheet
        fields=["batch",'topic','topic_status']
        widgets={
                    "batch":forms.Select(attrs={"class":"form-select"}),
                    "topic":forms.TextInput(attrs={"class":"form-control"}),
                    "topic_status":forms.Select(attrs={"class":"form-select"}),
                    # "date":forms.DateInput(attrs={"type":"date"}),
                }


    def clean(self):

            cleaned_data=super().clean()
            batch=cleaned_data["batch"]
            # date=cleaned_data["date"]
            # user = MyUser.objects.filter(user=self.request.user)
            # print(batch,date)
            print(self.user)
            record=TimeSheet.objects.filter(date=datetime.today(),batch=batch,user=self.user)
            if record:
                msg="already added"
                print(msg)
                self.add_error("topic",msg)







# sajay  22

# class SigninForm(forms.Form):
#     email=forms.CharField(widget=forms.EmailInput())
#     password=forms.CharField(widget=forms.PasswordInput())
#

