from django.shortcuts import render
from django.http import HttpResponse
def hi(request):
    return render(request,'firstapp/hello.html')
    #return HttpResponse('<h1>this is my first project</h1>')
# Create your views here.
