# Generated by Django 4.2 on 2023-05-02 13:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_blogs'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogs',
            options={'verbose_name_plural': 'مقالات و محتوا ساخته شده افراد '},
        ),
        migrations.AlterModelTable(
            name='blogs',
            table='Blogs',
        ),
    ]
