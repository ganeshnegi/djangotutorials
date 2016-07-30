from __future__ import unicode_literals

from django.db import models

class Student(models.Model):
	gender_choice = (('M','Male'),('F','Female'),)
	name = models.CharField(max_length=120)
	age=models.IntegerField(default=0)
	gender = models.CharField(max_length=1,choices=gender_choice,default='M')

	def __unicode__(self):
		return self.name
