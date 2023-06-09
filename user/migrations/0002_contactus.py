# Generated by Django 4.1.7 on 2023-04-18 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=50)),
                ('subject', models.CharField(max_length=30)),
                ('message', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'contactUs',
            },
        ),
    ]
