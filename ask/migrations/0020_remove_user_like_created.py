# Generated by Django 4.1.7 on 2023-04-25 14:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ask', '0019_rename_like_user_like_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_like',
            name='created',
        ),
    ]
