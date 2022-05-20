from django.shortcuts import render
from django.contrib.messages.views import SuccessMessageMixin

from django.views.generic import CreateView
from .models import UserData
from .forms import UserDataForm

# Create your views here.

class UserCreateView(SuccessMessageMixin,CreateView):
    form_class = UserDataForm
    model = UserData    
    success_message = 'Form Submitted Successfully.'

