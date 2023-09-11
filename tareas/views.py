from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.

def hola(self):
    return HttpResponse('<h2>Hola Mundo</h2> ' + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))