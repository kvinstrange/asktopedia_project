# Generated by Django 4.1.7 on 2023-04-06 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ask', '0009_alter_answers_docurl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='badges',
            name='rank',
            field=models.IntegerField(default=0),
        ),
    ]
