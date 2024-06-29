from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello(req):
    return render(req, "base/hello.html")

def index(req):
    return render(req, "base/index.html")