# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-09-17 07:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Exam', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exam',
            old_name='Answer',
            new_name='answer',
        ),
        migrations.RenameField(
            model_name='exam',
            old_name='Difficulty_level',
            new_name='difficulty_level',
        ),
        migrations.RenameField(
            model_name='exam',
            old_name='Option1',
            new_name='option1',
        ),
        migrations.RenameField(
            model_name='exam',
            old_name='Option2',
            new_name='option2',
        ),
        migrations.RenameField(
            model_name='exam',
            old_name='Option3',
            new_name='option3',
        ),
        migrations.RenameField(
            model_name='exam',
            old_name='Option4',
            new_name='option4',
        ),
        migrations.RenameField(
            model_name='exam',
            old_name='Question',
            new_name='question',
        ),
        migrations.RenameField(
            model_name='exam',
            old_name='Subject',
            new_name='subject',
        ),
    ]
