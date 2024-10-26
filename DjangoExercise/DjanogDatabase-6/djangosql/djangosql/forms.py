from django import forms 
from django.forms import ModelForm  
from djangosql.models import Employee

class EmployeeForm(forms.ModelForm):  
    class Meta:  
        model = Employee  
        fields = "__all__"  
        