# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django_extensions.admin import ForeignKeyAutocompleteAdmin

from .models import Exam


class ExamAdmin(ForeignKeyAutocompleteAdmin):
    model = Exam

    list_filter = ("difficulty_level","subject")
    list_display = ("question","answer","difficulty_level","subject")

admin.site.register(Exam,ExamAdmin)