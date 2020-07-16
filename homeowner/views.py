from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.http import HttpResponse 
from .models import Notification, Contact
from django.utils import timezone
from django.core.mail import send_mail


# Create your views here.
class Home(ListView):
    def get(self,request):
        return render(request, 'homeowner/index.html')

def NotifyHomeOwner(request):
    if request.method == "POST":
        notify_homeowner = Notification()
        email = request.POST['email']
        notify_homeowner.email = email
        notify_homeowner.pub_date = timezone.now()
        notify_homeowner.save()

        send_mail_homeowner(email, "this is subject Notification", "Hi this is my message body")

        context = {
            'email': notify_homeowner.email
        }
        return render(request, 'homeowner/thankyou.html', context)


def send_mail_homeowner(email, subject, message):
    obj = send_mail(subject,message,'jarquevious.nelson@students.makeschool.com',[email], fail_silently=False)
    print("Email sent!")

def ContactInquiry(request):
    if request.method == "POST":
        contact_inquiry = Contact()
        contact_inquiry.name = request.POST['name']
        contact_inquiry.email = request.POST['email']
        contact_inquiry.subject = request.POST['subject']
        contact_inquiry.message = request.POST['message']
        contact_inquiry.pub_date = timezone.now()
        contact_inquiry.save()

        context = {
            'name': contact_inquiry.name,
            'email': contact_inquiry.email
        }
        return render(request, 'homeowner/thankyou.html', context)
