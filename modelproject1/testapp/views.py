from django.shortcuts import render
from testapp import models
# Create your views here.

def employee_view(request):
    employees = models.Employee.objects.all()

    return render(request,'testapp/results.html',{'employees':employees})
