from django.shortcuts import render
from .models import Skills,Language

def skills(request):
    context = {
        'skill' : Skills.objects.all(),
        'language' : Language.objects.all(),
        }
    return render(request,'skills/skills.html',context)
