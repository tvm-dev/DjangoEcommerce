#coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm
from django.views.generic import View, TemplateView



class IndexView(TemplateView):

    template_name = 'index.html'

index = IndexView.as_view()

# def index(request):
#     return render(request, 'index.html')

def contact(request):
    success = False
    form = ContactForm(request.POST or None)
    if form.is_valid():
       form.send_mail()   
       sucess = True
    context = {
      'form': form,
      'success': success
  }
    return render(request, 'contact.html', context)            