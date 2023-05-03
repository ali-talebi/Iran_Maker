# Generated by Django 4.2 on 2023-05-02 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_posts_picture1_posts_picture2_posts_picture3'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='picture1',
            field=models.FileField(blank=True, null=True, upload_to='Article_picture/', verbose_name='1عکس سر تیتر '),
        ),
        migrations.AlterField(
            model_name='posts',
            name='picture2',
            field=models.FileField(blank=True, null=True, upload_to='Article_picture/', verbose_name='2عکس سر تیتر '),
        ),
        migrations.AlterField(
            model_name='posts',
            name='picture3',
            field=models.FileField(blank=True, null=True, upload_to='Article_picture/', verbose_name='3عکس سر تیتر '),
        ),
    ]