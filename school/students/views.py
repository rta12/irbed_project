from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import Student

# Create your views here.
def hello(request):
    student = Student(first_name="farah", last_name="ahmad", avg=70.0, age=30)
    student.save()
    return HttpResponse("hello")

def hi(requset):
    data = Student.objects.all()
    return HttpResponse(data[1].first_name + "\t" + data[2].last_name + "\t" + str(data[1].avg) + "\t" + str(data[1].age))


def stdlist(request):
    t = loader.get_template('first.html')
    return HttpResponse(t.render())

def second(request):
    template = loader.get_template('second.html')
    return HttpResponse(template.render())

def newlist(request):
    data = Student.objects.all()
    template = loader.get_template('table.html')
    ctx = {
        'data' : data,
        'test' : 'hello'

    }
    return HttpResponse(template.render(ctx, request))