from django.contrib import admin
from .models import Skills,Language

class SkillsAdmin(admin.ModelAdmin):
    list_display = ['skill_name','skill_percentage']

admin.site.register(Skills,SkillsAdmin)

class LanguagesAdmin(admin.ModelAdmin):
    list_display = ['language_name','language_percentage']

admin.site.register(Language,LanguagesAdmin)
