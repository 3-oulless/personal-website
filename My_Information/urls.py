from django.urls import path
from .views import information

app_name = 'My_Information'

urlpatterns = [
    path('',information,name='information')
]