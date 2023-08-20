from django.contrib import admin
from .models import Information,Social_Media_followers

class InformationAdmin(admin.ModelAdmin):
    list_display = ['full_name','img','berth_day','website','phone','job']

admin.site.register(Information, InformationAdmin)

class Social_Media_followersAdmin(admin.ModelAdmin):
    list_display = ['social_media_name','Social_Media_follower_count']

admin.site.register(Social_Media_followers, Social_Media_followersAdmin)