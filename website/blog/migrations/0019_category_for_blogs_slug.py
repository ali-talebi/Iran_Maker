# Generated by Django 4.2 on 2023-05-02 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_category_for_blogs'),
    ]

    operations = [
        migrations.AddField(
            model_name='category_for_blogs',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, null=True, unique=True, verbose_name='آدرس دسته بندی ها '),
        ),
    ]
