from django.forms import ModelForm
from django import forms

from formvalidation.models import User

class UserForm(ModelForm):

   # meta data for displaying a form
   class Meta:
      # model
      model = User

      # displaying fields
      fields = '__all__'

   # method for cleaning the data
   def clean(self):
      super(UserForm, self).clean()

      # getting username and password from cleaned_data
      username = self.cleaned_data.get('username')
      password = self.cleaned_data.get('password')

      # validating the username and password
      if len(username) < 5:
         self._errors['username'] = self.error_class(['A minimum of 5 characters is required'])

      if len(password) < 8:
         self._errors['password'] = self.error_class(['Password length should not be less than 8 characters'])

      return self.cleaned_data