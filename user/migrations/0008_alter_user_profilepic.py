# Generated by Django 4.1.7 on 2023-04-26 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_delete_contactus_user_age_user_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profilepic',
            field=models.ImageField(blank=True, default='media/avatar7.png', null=True, upload_to='image/'),
        ),
    ]