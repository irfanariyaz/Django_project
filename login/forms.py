from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Classifields,Subcategory,Category




class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

#create a form to select category and subcategory and add that to the ClassifieldForm


class ClassifieldForm(forms.ModelForm):

    class Meta:
        model = Classifields
        fields = ['category','subcategory','location','title','description','price','phone_no','image']

