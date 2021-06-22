from django import forms
from django.forms import widgets
from .models import stud
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget 

class DateInput(forms.DateInput):
    input_type = 'date'

class   StudForm(forms.Form):
   
    name = forms.CharField(max_length=30,label= "Name")
   
    contact = PhoneNumberField(
        widget = PhoneNumberPrefixWidget(initial='IN')
    )
    email = forms.EmailField(max_length=30,label= "Email i'd")
    dob = forms.DateField(widget=DateInput ,label= "Date of Birth") #
    

class Sform(forms.Form):
    name = forms.CharField(max_length=30,label= "Name")
