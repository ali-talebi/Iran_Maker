# Generated by Django 4.2 on 2023-05-01 17:10

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_contact_members_alter_service_category_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان')),
                ('slug', models.SlugField(max_length=200, unique=True, verbose_name='آدرس  ')),
                ('picture', models.FileField(blank=True, null=True, upload_to='Article_picture', verbose_name='عکس سر تیتر ')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='زمان انتشار ')),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('p', 'منتشر شود '), ('d', 'پیش نویس باقی بماند ')], default='d', max_length=1, verbose_name='وضعیت')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.members', verbose_name='نویسنده')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.service_category', verbose_name='دسته بندی ')),
            ],
            options={
                'verbose_name_plural': 'محتوا سایت ',
                'db_table': 'Posts',
            },
        ),
    ]
