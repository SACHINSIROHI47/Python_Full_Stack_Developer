from django import forms
from django.utils.safestring import mark_safe  
# creating a form 

class NameForm(forms.Form):
    your_name = forms.CharField(label=mark_safe("Enter your Name "), max_length=100)
    address=forms.CharField(label=mark_safe("</br></br>Enter your Address "),max_length=100)
