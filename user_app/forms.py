from django import forms
from .models import UserData

class UserDataForm(forms.ModelForm):

    class Meta:
        model = UserData
        fields = ['name','email']

    def clean(self):
        cleaned_data = super(UserDataForm,self).clean()
        cleaned_data.get('email')       
        return cleaned_data    