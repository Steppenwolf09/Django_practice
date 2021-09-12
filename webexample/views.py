from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(reauest):
     return HttpResponse (",<h3>Hi, world!,</h3>")