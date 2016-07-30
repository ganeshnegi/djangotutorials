from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
# Create your views here.
def details(request):
	ctx={}
	students=Student.objects.all()
	ctx['students']=students
	return render(request, 'datatables/student_details.html',ctx)

