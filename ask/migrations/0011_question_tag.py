# Generated by Django 4.1.7 on 2023-04-06 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ask', '0010_alter_badges_rank'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='tag',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
