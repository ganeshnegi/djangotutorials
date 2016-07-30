from django.conf.urls import url, include
from django.contrib import admin
from .views import csv_file_upload

urlpatterns = [
    url(r'upload/$', csv_file_upload, name='csv_file_upload'),
]