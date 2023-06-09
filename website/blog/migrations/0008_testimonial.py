# Generated by Django 4.2 on 2023-05-02 11:12

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_members_instagram_members_linkedin'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.IntegerField(blank=True, null=True, verbose_name='امتیاز')),
                ('message', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='متن پیام')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.members', verbose_name='فرد مورد نظر ')),
            ],
        ),
    ]
