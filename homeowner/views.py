from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.http import HttpResponse 
from .models import Notification, Contact
from django.utils import timezone
from django.core.mail import send_mail, EmailMultiAlternatives
from django.conf import settings
from django.template.loader import get_template


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

        send_email_attach(email, "Welcome to our newsletter", 
                            "Hi this is my message body", notify_homeowner.id)

        context = {
            'email': notify_homeowner.email
        }
        return render(request, 'homeowner/thankyou.html', context)

def send_email_attach(email, subject, msg, id):
    message = EmailMultiAlternatives(subject=subject, body=msg,from_email='jarquevious.nelson@students.makeschool.com', to=[email])
    html_templ = get_template("email/welcome.html").render({'id':id, "email":email})
    message.attach_alternative(html_templ, "text/html")
    message.send()
    print("message sent")

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


def Unsubscribe(request, id):
    Notification.objects.filter(id=id).delete()
    return render(request, 'homeowner/unsubscribe.html')