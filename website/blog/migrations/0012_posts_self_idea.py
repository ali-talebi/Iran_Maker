# Generated by Django 4.2 on 2023-05-02 12:03

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_members_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='self_idea',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name=' نظرات طراح در مورد طرح  '),
        ),
    ]
