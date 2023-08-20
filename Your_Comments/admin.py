from django.contrib import admin
from .models import Comments


class CommentsAdmin(admin.ModelAdmin):
    list_display = ['full_name','job','email','subject','show_massage']
admin.site.register(Comments, CommentsAdmin)
