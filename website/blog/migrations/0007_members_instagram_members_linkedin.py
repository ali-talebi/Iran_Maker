# Generated by Django 4.2 on 2023-05-01 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_members_picture_alter_members_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='members',
            name='instagram',
            field=models.CharField(blank=True, max_length=200, null=True, unique=True, verbose_name='آدرس اینستاگرام '),
        ),
        migrations.AddField(
            model_name='members',
            name='linkedin',
            field=models.CharField(blank=True, max_length=200, null=True, unique=True, verbose_name='آدرس لینک دین '),
        ),
    ]
