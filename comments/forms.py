from django import forms
from comments import models
class UserCumment(forms.ModelForm):
    class Meta():
        model = models.Comments
        fields = ["name","family","message"]