from django.contrib.auth.forms import UserCreationForm , SetPasswordForm ,UserChangeForm
from django import forms
from django.contrib.auth import get_user_model


class RegisterForm(UserCreationForm):
    email = forms.CharField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    password1 = forms.CharField()
    password2 = forms.CharField()

    class Meta:
        model = get_user_model()
        fields = ["first_name","last_name","username","email","password1","password2"]



class ChangePasswordForm(SetPasswordForm):
    class Meta:
        model = get_user_model()
        fields = ['new_password1', 'new_password2']




class ProfileUpdate(UserChangeForm):
    password = None

    class Meta:
        model = get_user_model()
        fields = ('username','first_name','last_name','email')