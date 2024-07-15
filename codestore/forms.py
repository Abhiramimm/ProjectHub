from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm

from django import forms

from codestore.models import Project

class SignUpForm(UserCreationForm):

    class Meta:

        model=User

        fields=["username","email","password1","password2"]

class SignInForm(forms.Form):

    username=forms.CharField()

    password=forms.CharField()

class ProjectForm(forms.ModelForm):

    class Meta:

        model=Project

        fields="__all__"

        widgets={

            "title":forms.TextInput(attrs={"class":"form-control mb-3"}),

            "description":forms.TextInput(attrs={"class":"form-control mb-3"}),

            "github_link":forms.TextInput(attrs={"class":"form-control mb-3"}),

            "image":forms.ClearableFileInput(attrs={"class":"form-control mb-3"}),
            
            "project_preview":forms.ClearableFileInput(attrs={"class":"form-control mb-3"})
        }


