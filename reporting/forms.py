from django.forms import ModelForm
from reporting.admin import UserCreationForm
from reporting.models import MyUser,Course,Batch
from django import forms


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
            "course": forms.TextInput(attrs={"class": "form-control"}),
            "batch_name": forms.TextInput(attrs={"class": "form-control"}),

        }
