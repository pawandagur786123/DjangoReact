# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-09-17 06:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Question', models.CharField(max_length=100)),
                ('Option1', models.CharField(max_length=100)),
                ('Option2', models.CharField(max_length=100)),
                ('Option3', models.CharField(max_length=100)),
                ('Option4', models.CharField(max_length=100)),
                ('Answer', models.CharField(max_length=100)),
                ('Subject', models.PositiveIntegerField(blank=True, choices=[(1, 'Math'), (2, 'Science')], null=True)),
                ('Difficulty_level', models.PositiveIntegerField(blank=True, choices=[(1, 'Low'), (2, 'Medium'), (3, 'High')], null=True)),
            ],
        ),
    ]
