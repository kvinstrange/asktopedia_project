# Generated by Django 4.1.7 on 2023-04-24 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_user_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profilepic',
            field=models.ImageField(blank=True, default='media/avatar7.png', null=True, upload_to='image'),
        ),
    ]
