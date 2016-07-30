from django.conf.urls import url, include
from django.contrib import admin
from .views import details

urlpatterns = [
    url(r'details/$', details, name='student_details'),
]