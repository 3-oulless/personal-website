from django.shortcuts import render
from My_Information.models import Information,Social_Media_followers
from Skills.models import Skills,Language
import datetime

def header(request,*args,**kwargs):
    context = {'information' : Information.objects.all()}
    return render(request,'shared/Header.html', context)

def home(request):
    information = Information.objects.all()


    obj = datetime.datetime.today()
    time_year_now = obj.year
    year_str = 0

    for i in information:
        year = str(i.berth_day)
        # i.visit_count += 1
        # i.save()
    age = time_year_now - int(year[:4])
    context = {
        'information' : information,
        'berth_day': age,
        'social_media' : Social_Media_followers.objects.all(),
        'skill' : Skills.objects.all(),
        'language' : Language.objects.all(),
        }
    return render(request,'home.html', context)