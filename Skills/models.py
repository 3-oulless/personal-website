from django.db import models

class Skills(models.Model):
    skill_name = models.CharField(max_length=20,verbose_name='نام مهارت خود را وارد کنید')
    skill_percentage = models.IntegerField(default=0, verbose_name='درصد مهارت خود را وارد کنید')

    def __str__(self):
        return self.skill_name

class Language(models.Model):
    language_name = models.CharField(max_length=20,verbose_name='نام زبانی که میتوانید صحبت کنید را وارد کنید')
    language_percentage = models.IntegerField(default=0, verbose_name='درصد تسلط خود بر روی زبان مورد نظر را وارد کنید')