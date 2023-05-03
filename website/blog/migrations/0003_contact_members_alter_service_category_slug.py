# Generated by Django 4.2 on 2023-05-01 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_service_category_options_service_category_slug_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=400, verbose_name='نام و نام خانوادگی ')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان')),
                ('email', models.EmailField(max_length=254, verbose_name='ایمیل')),
                ('file', models.FileField(upload_to='Cantact_with_me', verbose_name='فایل')),
            ],
            options={
                'verbose_name_plural': 'ارتباط با ما ',
                'db_table': 'Contact',
            },
        ),
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=200, verbose_name='نام')),
                ('lastname', models.CharField(max_length=200, verbose_name='نام خانوادگی')),
                ('birthday', models.DateTimeField(verbose_name='تاریخ تولد ')),
                ('phone_number', models.IntegerField(verbose_name='شماره تلفن ')),
                ('code_melli', models.IntegerField(verbose_name='کد ملی ')),
                ('education_level', models.CharField(choices=[('d', 'دیپلم'), ('b', 'لیسانس'), ('m', 'فوق لیسانس'), ('p', 'دکترا')], max_length=1, verbose_name='تحصیلات  ')),
            ],
            options={
                'verbose_name_plural': 'اعضا',
                'db_table': 'Members',
            },
        ),
        migrations.AlterField(
            model_name='service_category',
            name='slug',
            field=models.SlugField(max_length=200, null=True, verbose_name='آدرس مقاله '),
        ),
    ]
