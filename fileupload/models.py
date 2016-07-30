from __future__ import unicode_literals

from django.db import models

class Document(models.Model):
	file_name = models.CharField(max_length=120)
	doc_file = models.FileField(upload_to='document')
	
	def __unicode__(self):
		return self.file_name
