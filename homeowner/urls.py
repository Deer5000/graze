from django.urls import path
from . import views
app_name = 'homeowner'
urlpatterns = [
    path('',views.Home.as_view(), name='home'),
    path('notify/',views.NotifyHomeOwner, name='notify'),
    path('contact/',views.ContactInquiry, name='contact'),
    path('unsubscribe/<str:id>',views.Unsubscribe, name='unsubscribe'),
    
    
]
