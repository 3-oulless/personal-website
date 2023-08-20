from django import http
from django.shortcuts import redirect, render
from .forms import CommentForm
from My_Information.models import Information
from .models import Comments

def comment(request):
    context = {
        'comments':Comments.objects.filter(show_massage=True)
        }
    return render(request,'comments/comments.html',context)

def CommentForms(requset):
    comment_form = CommentForm(requset.POST or None)
    if comment_form.is_valid():
        full_name = comment_form.cleaned_data.get('full_name')
        job = comment_form.cleaned_data.get('job')
        email = comment_form.cleaned_data.get('email')
        subject = comment_form.cleaned_data.get('subject')
        comment = comment_form.cleaned_data.get('comment')
        show_massage = comment_form.cleaned_data.get('show_massage')
        Comments.objects.create(full_name=full_name,job=job,email=email,subject=subject,comment=comment,show_massage=show_massage)
        return redirect('/your-comments/forms')

    context = {
        'comment_form':comment_form,
        'information':Information.objects.all(),
        }
    return render(requset,'comments/forms.html',context)


