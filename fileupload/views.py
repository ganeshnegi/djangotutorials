from django.shortcuts import render, render_to_response, RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from .forms import DocumentForm
from .models import Document
from django.core.urlresolvers import reverse

def csv_file_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(doc_file = request.FILES['doc_file'])
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('csv_file_upload'))
    else:
    	form = DocumentForm() # A empty, unbound form
    documents = Document.objects.all()

    return render_to_response('fileupload/upload_file.html',{'documents': documents, 'form': form},context_instance=RequestContext(request))
