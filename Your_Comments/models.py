import email
from django.db import models

class Comments(models.Model):
    full_name = models.CharField(max_length=100,verbose_name='نام و نام خانوادگی')
    job = models.CharField(max_length=50,verbose_name='شغل')
    email = models.EmailField(verbose_name='ایمیل خود را وارد کنید ')
    subject = models.CharField(max_length=150,verbose_name='عنوان')
    comment = models.TextField(verbose_name='سخن خود')
    show_massage = models.BooleanField(default=False,verbose_name='آیا میخواهید پیام شما برای دیگران نمایش داده شود ؟')

    def __str__(self):
        return f'{self.full_name}-{self.job}-{self.comment[:80]}'
