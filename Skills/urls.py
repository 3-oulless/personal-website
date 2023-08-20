from django.urls import path
from .views import skills
app_name = 'Skills'

urlpatterns = [
    path('',skills,name='skills')
]