# Generated by Django 4.2 on 2023-05-01 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='service_category',
            options={'verbose_name_plural': 'خدمات'},
        ),
        migrations.AddField(
            model_name='service_category',
            name='slug',
            field=models.CharField(max_length=200, null=True, verbose_name='آدرس مقاله '),
        ),
        migrations.AlterModelTable(
            name='service_category',
            table='Service',
        ),
    ]
