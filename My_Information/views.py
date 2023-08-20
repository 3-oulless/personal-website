from datetime import time
from django.shortcuts import render
from .models import Information,Social_Media_followers
import datetime

def information(request):
    information = Information.objects.all()

    obj = datetime.datetime.today()
    time_year_now = obj.year
    year_str = 0

    for i in information:
        year = str(i.berth_day)
    
    age = time_year_now - int(year[:4])
    context = {
        'information' : information,
        'berth_day': age,
        'social_media' : Social_Media_followers.objects.all()
        }
    return render(request,'information/informations.html',context)
