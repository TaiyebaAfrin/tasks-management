from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Hello, this is the home page!")
def contact(request):
    return HttpResponse("<h3 style: 'color: gray'>Hello, this is the contact page</h3>")

def show_task(request):
    return HttpResponse("<h3>Hello, this is the task</h3>")

