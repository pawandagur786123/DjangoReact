# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Exam(models.Model):
	TYPE_MATH = 1
	TYPE_SCIENCE = 2
	TYPE_OPTIONS = (
	    (1, 'Math'),
	    (2, 'Science')
	)
	subject = models.PositiveIntegerField(choices=TYPE_OPTIONS, null=True, blank=True)

	TYPE_LOW = 1
	TYPE_MEDIUM = 2
	TYPE_HIGH = 3
	TYPE_LEVEL = (
	    (1, 'Low'),
	    (2, 'Medium'),
	    (3, 'High')
	)    
	difficulty_level = models.PositiveIntegerField(choices=TYPE_LEVEL, null=True, blank=True)
	question = models.CharField(max_length=100)
	option1 = models.CharField(max_length=100)
	option2 = models.CharField(max_length=100)
	option3 = models.CharField(max_length=100)
	option4 = models.CharField(max_length=100)
	answer = models.CharField(max_length=100)


