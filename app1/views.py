from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def specific1(request):
    return HttpResponse('<h1>Jai Balayaa</h1>')


def specific2(request):
    return HttpResponse('<h1>Jai Mallareddy</h1>')