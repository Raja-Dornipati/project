from django import forms
# from django.contrib.auth.models import User
from employee.models import *
from django.core.validators import validate_email
from django.core import validators
from django.core.validators import RegexValidator
from django.contrib.auth.password_validation import validate_password



class Post_Form(forms.Form):
    alpha = RegexValidator(regex='^[a-z A-Z]*$', message='must be in charecters only')

    title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Title'}),validators=[alpha],required=True)
    catagory = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control', 'placeholder':'select an option'}),required=True)
    description = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter the text here'}),required=True)


class Post_replyform(forms.Form):
    description = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=True)





class Registrationform(forms.ModelForm):
    alpha = RegexValidator(regex='^[a-z A-Z]*$',message='name  must be in charecters only')
    user_validate = RegexValidator(regex='^[a-z A-Z 0-9]*$',message='username must be in charecters and numbers only')
    # numeric = RegexValidator(regex='^[0-9]*$',message='last name must be in charecters')
    phone_regex = RegexValidator(regex='^[\+?1?\d{9,15}]*$',message="Phone number must be entered in the correct format")
    username  = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'enter username'}), validators=[user_validate], max_length=30)
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'enter first name'}), validators=[alpha], max_length=100)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'enter last name'}),validators=[alpha], max_length=100)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'enter mail id'}), required=True, max_length=100)
    phone = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'enter phone number'}), validators=[phone_regex], max_length=50)
    # gender = forms.ChoiceField()
    # city = forms.ChoiceField()
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'enter password'}), required=True, max_length=100)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'confirm password'}), required=True, max_length=100)

    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'email',
                  'phone', 'gender', 'city', 'password', 'password1']


    def clean_username(self):
        emp_user = self.cleaned_data.get('username')
        try:
            match = Profile.objects.get(username = emp_user)
        except:
            return self.cleaned_data['username']
        raise forms.ValidationError("Name already exsits")



    def clean_email(self):
        emp_email = self.cleaned_data["email"]
        try:
            mt = Profile.objects.get(email=emp_email)
        except:
            return self.cleaned_data["email"]
        raise forms.ValidationError("Email already exists")
        # return email
    def clean_password1(self):
        pas = self.cleaned_data['password']
        pas1 = self.cleaned_data['password1']
        MIN_LENGTH = 8
        if pas and pas1:
            if pas != pas1:
                raise forms.ValidationError("Password and Confirm password not matched")
            else:
                if len(pas) < MIN_LENGTH:
                    raise forms.ValidationError("Password should have atleast %d charecters " % MIN_LENGTH)
                if pas.isdigit():
                    raise forms.ValidationError("Password should not all numeric")
        return pas1









# class UserForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput)
#
#     class Meta:
#         model = User
#         fields = ['first_name', 'last_name',
#                   'email', 'username', 'password']
#
#         label = {'password':'password'}
#
#
#     def save(self):
#         password = self.cleaned_data.pop('password')
#         u = super().save()
#         u.set_password(password)
#         u.save()
#         return u
