from urllib.parse import MAX_CACHE_SIZE
from django.db import models

class Information(models.Model):

    class Degree_Choice(models.TextChoices):
        Junior = "Junior"
        Middle_Level = "Middle_Level"
        Senior = "Senior"

    full_name = models.CharField(max_length=20,verbose_name='نام و نام خانوادگی')
    img = models.ImageField(upload_to='picture', verbose_name='آواتار خود را انتخاب کنید')
    berth_day = models.DateField(verbose_name='تاریخ تولد خود را انتخاب کنید')
    website = models.URLField(verbose_name='وب سایت خود را وارد کنید ')
    phone = models.CharField(max_length=15,verbose_name='شماره تماس خود را وارد کنید')
    job = models.CharField(max_length=100,verbose_name='در چه زمینه ای کار میکنید ',blank=True,null=True)
    city = models.CharField(max_length=15,verbose_name='محل زندگی خود را وارد کنید')
    location = models.CharField(max_length=200,verbose_name="آدرس محل زندگی خود را وارد کنید",default=True)
    degree = models.CharField(max_length=20,choices=Degree_Choice.choices,verbose_name='سطح مهارت خود را وارد کنید')
    email = models.EmailField(max_length=30,verbose_name='ایمیل خود را وارد کنید')
    freelance = models.BooleanField(default=False,verbose_name='آیا میتوانید به صورت آزادانه کار کنید ')
    description = models.TextField(max_length=500,verbose_name='توضیحات در مورد خود ')

    twitter = models.CharField(max_length=50,verbose_name='آدرس حساب کاربری توییتر خود را وارد کنید')
    instagram = models.CharField(max_length=50,verbose_name='آدرس حساب کاربری اینستاگرام خود را وارد کنید')
    facebook = models.CharField(max_length=50,verbose_name='آدرس حساب کاربری فیس بوک خود را وارد کنید')
    github = models.CharField(max_length=50,verbose_name='آدرس حساب کاربری گیت هاب خود را وارد کنید')
    visit_count = models.IntegerField(verbose_name="تعداد بازدید",default=0)

    def __str__(self):
        return self.full_name


class Social_Media_followers(models.Model):
    social_media_name = models.CharField(max_length=20,verbose_name='نام پلتفرم مورد نظر را وارد کنید')
    Social_Media_follower_count = models.IntegerField(default=0,verbose_name='تعداد فالور خود را وارد کنید')

    def __str__(self):
        return self.social_media_name