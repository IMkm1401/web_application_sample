from . import models
from django import forms
class UserForm(forms.ModelForm):
    class Meta():
        model = models.UserInformation
        fields = ["subject","name","family","email_address","phone_number","user_email"]