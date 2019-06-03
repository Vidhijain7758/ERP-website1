from django import forms
from django.contrib.auth import authenticate
from datetime import date
class LoginForm(forms.Form):
    username=forms.CharField(max_length=15)
    password=forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        user=self.cleaned_data.get("username")
        passw=self.cleaned_data.get("password")
        usern=authenticate(username=user,password=passw)
        if usern is None:
            raise forms.ValidationError("wrong credentials")


from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError
from .models import quality

class CustomUserCreationForm(forms.Form):

    username = forms.CharField(label='Enter Username', max_length=150)
    first_name=forms.CharField(label='Enter Firstname', max_length=150)
    last_name = forms.CharField(label='Enter Lastname', max_length=150)
    #user_id = forms.CharField(label = 'line number',maxlength = 10 )

    email = forms.EmailField(label='Enter email')
    password1 = forms.CharField(label='Enter password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)
    #factory_name = forms.CharField(label ='enter factory name ',max_length=20)
    #category = forms.CharField(label =' category',max_length=30)
    #sub_category = forms.CharField(label ='sub-category',max_length=40)
    #department = forms.CharField(label ='department',max_length=40)
    #section = forms.CharField(label ='section',max_length=40)
    #item_no = forms.IntegerField(label ='item no.')
    #style_name = forms.CharField(label ='style name',max_length=40)
    #style_number = forms.IntegerField(label ='style number')
    #line_no =forms.CharField(label ='line no',max_length =40)

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
            #user_id = self.cleaned_data['user_id'])
            #factoryname = self.cleaned_data['factory_name'],
            #category = self.cleaned_data['category'],
            #sub_category = self.cleaned_data['sub_category'],
            #department = self.cleaned_data['department'],
            #section = self.cleaned_data['section'],

            #item_no = self.cleaned_data['item_no'],

            #style_name = self.cleaned_data['style_name'],

            #style_no = self.cleaned_data['style_number'],
            #line_no = self.cleaned_data['line_no'] ,)

        return user

class ABC(forms.Form):
    Date = forms.DateField(widget=forms.SelectDateWidget)

    b = ('EP_1', 'EP_2', 'EP_3', 'EP_4', 'EP_5', 'EP_6', 'EP_7', 'EP_8', 'EP_9', 'EP_10','EP_11', 'EP_12', 'EP_13', 'EP_14','EP_15', 'EP_16', 'EP_17', 'EP_18', 'EP_19', 'EP_20', 'EP_21', 'EP_22', 'EP_23', 'EP_24')
    #name = forms.CharField(label ='user name',maxlength = 20)
    factoryname = forms.CharField(label='enter factory name ', max_length=20)
    category = forms.CharField(label=' category', max_length=30)
    sub_category = forms.CharField(label='sub-category', max_length=40)
    department = forms.CharField(label='department', max_length=40)
    section = forms.CharField(label='section', max_length=40)
    item_no = forms.IntegerField(label='item no.')
    style_name = forms.CharField(label='style name', max_length=40)
    style_no = forms.IntegerField(label='style number')
    line_no = forms.CharField(label='line no', max_length=40)

    total_defects = forms.IntegerField(label ='enter the total defects')
    total_checked = forms.IntegerField(label ='enter the total checked')
    total_passed = forms.IntegerField(label ='enter the total passed')

class QueryForm(forms.Form):
    factoryname = forms.CharField(label='enter your factory name')
    category = forms.CharField(label ='enter category of product')
    sub_category = forms.CharField(label ='sub-category')
    department = forms.CharField(label ="enter department")
    section = forms.CharField(label ='enter section')
    item_no = forms.IntegerField(label ="enter the item no.")
    style_name = forms.CharField(label ='enter the name of your style')
    style_no = forms.IntegerField(label = 'enter the style number')

    for_date = forms.DateField(required=True,label="Select Date For Which DHU Is Needed :",widget = forms.SelectDateWidget())

class QueryForm2(forms.Form):
   # b = ['EP_1', 'EP_2', 'EP_3', 'EP_4', 'EP_5', 'EP_6', 'EP_7', 'EP_8', 'EP_9', 'EP_10', 'EP_11', 'EP_12', 'EP_13', 'EP_14','EP_15', 'EP_16', 'EP_17', 'EP_18', 'EP_19', 'EP_20', 'EP_21', 'EP_22', 'EP_23', 'EP_24']

    line_no = forms.CharField(required = True,label ="enter the line number")
    factoryname = forms.CharField(label='enter your factory name')
    category = forms.CharField(label ='enter category of product')
    sub_category = forms.CharField(label ='sub-category')
    department = forms.CharField(label ="enter department")
    section = forms.CharField(label ='enter section')
    item_no = forms.IntegerField(label ="enter the item no.")
    style_name = forms.CharField(label ='enter the name of your style')
    style_no = forms.IntegerField(label = 'enter the style number')
    #g = User.objects.get







