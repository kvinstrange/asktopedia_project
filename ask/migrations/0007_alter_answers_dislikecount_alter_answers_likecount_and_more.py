# Generated by Django 4.1.7 on 2023-04-05 04:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ask', '0006_alter_answers_dislikecount_alter_answers_likecount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answers',
            name='dislikeCount',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='answers',
            name='likeCount',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='answers',
            name='markAsSolution',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='answers',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ask.question'),
        ),
        migrations.AlterField(
            model_name='answers',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
