from django import forms
from django.contrib.auth import authenticate
from datetime import date
from django.forms import ModelForm
from django import forms
from .models import order, product
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError

class LoginForm(forms.Form):

    username=forms.CharField(max_length=15)
    password=forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        user=self.cleaned_data.get("username")
        passw=self.cleaned_data.get("password")
        usern=authenticate(username=user,password=passw)
        if usern is None:
            raise forms.ValidationError("wrong credentials")


class CustomUserCreationForm(forms.Form):
    choices =  [('student', 'student'), ('cafeteria', 'cafeteria'), ('lost and found', 'lost_and_found'), ('swachh bharat', 'swachh_bharat'), ('events manager', 'events')]
    username = forms.CharField(label='Enter Username', max_length=150)
    first_name=forms.CharField(label='Enter name', max_length=150)



    email = forms.EmailField(label='Enter email')
    password1 = forms.CharField(label='Enter password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)
    last_name = forms.CharField(label = 'last name',max_length= 150)


    class Meta:
        model=User
        fields={'username','first_name','last_name','e-mail','password1','password2'}


    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.count():
            raise  ValidationError("Username already exists")
        return username

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise  ValidationError("Email already exists")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Password don't match")

        return password2

    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password1'],
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'])

        return user


class select2(forms.Form):
    choices = [('student', 'student'), ('cafeteria', 'cafeteria'), ('lost_and_found', 'lost_and_found'), ('swachh', 'swachh')]
    sele = forms.ChoiceField(label ='LOGIN AS :',choices = choices)




class OrderForm(forms.Form):
    OPTIONS = (
        ('Postpay','Postpay'),
        ('Prepay (Full)','Prepay (Full)')

    )
    name = forms.CharField(label = 'enter name' )
    phone = forms.IntegerField(label ='enter phone number')
    address = forms.CharField(label = 'address')

    payment_option = forms.ChoiceField(choices=OPTIONS)
    product_id = forms.ModelChoiceField(queryset=product.objects.filter(active='1'), empty_label='')

    quantity = forms.IntegerField(initial=1)



class ProductForm(forms.Form):

    product_name =forms.CharField(label = 'product name')
    product_details =forms.CharField(label = 'product details')
    price = forms.IntegerField(label ='price')
