from django.urls import path
from .views import comment,CommentForms

app_name = 'Your_Comments'

urlpatterns = [
    path('',comment,name='comments'),
    path('forms/',CommentForms,name='CommentForms')
]