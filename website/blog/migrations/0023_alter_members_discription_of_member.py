# Generated by Django 4.2 on 2023-05-03 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0022_members_discription_of_member'),
    ]

    operations = [
        migrations.AlterField(
            model_name='members',
            name='discription_of_member',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='متن درباره فرد '),
        ),
    ]
