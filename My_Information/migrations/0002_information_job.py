# Generated by Django 4.1.2 on 2022-10-21 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('My_Information', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='information',
            name='job',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='در چه زمینه ای کار میکنید '),
        ),
    ]