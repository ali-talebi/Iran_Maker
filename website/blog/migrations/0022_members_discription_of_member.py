# Generated by Django 4.2 on 2023-05-03 06:58

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0021_blogs_head_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='members',
            name='discription_of_member',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='متن درباره فرد '),
        ),
    ]
