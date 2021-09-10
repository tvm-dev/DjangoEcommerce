from django.shortcuts import render
from django.views.generic import CreateView
#from django.urls import reverse

from .models import User
from .forms import UserAdminCreationForm

class RegisterView(CreateView):
    model = User
    template_name = 'accounts/register.html'
    form_class = UserAdminCreationForm
    #success_url = 'index'
    success_url = '/'

register = RegisterView.as_view()




