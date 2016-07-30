from django import forms
from .models import Document

class DocumentForm(forms.Form):
	file_name = forms.CharField(max_length=120)
	doc_file = forms.FileField(label='Select a file')