# Generated by Django 4.1.7 on 2023-03-17 04:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=1000)),
                ('likeCount', models.IntegerField()),
                ('dislikeCount', models.IntegerField()),
                ('markAsSolution', models.IntegerField()),
                ('docUrl', models.CharField(max_length=250)),
            ],
            options={
                'db_table': 'answers',
            },
        ),
        migrations.CreateModel(
            name='Badges',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('badgetitle', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=300)),
                ('rank', models.IntegerField()),
            ],
            options={
                'db_table': 'badges',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('description', models.CharField(max_length=1000)),
                ('status', models.IntegerField()),
            ],
            options={
                'db_table': 'question',
            },
        ),
        migrations.CreateModel(
            name='TechnologyLabel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=25)),
            ],
            options={
                'db_table': 'technology_label',
            },
        ),
        migrations.CreateModel(
            name='Tutorials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=250)),
                ('isApproved', models.IntegerField()),
                ('rejectReason', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'tutorials',
            },
        ),
        migrations.CreateModel(
            name='User_Badges',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('earnDate', models.DateField(auto_now_add=True)),
                ('badge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ask.badges')),
            ],
            options={
                'db_table': 'user_badges',
            },
        ),
    ]