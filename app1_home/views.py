from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def welcome(Request):
    return HttpResponse("<h1 style='background:red;'> "hello krishnanna" </h1>")