from django.shortcuts import render
from django.http import HttpResponse
import datetime
import time


# Create your views here.
def home(request):
    return HttpResponse('you are welcome.')

def today(request):
    date= datetime.date.today()
    return HttpResponse("Todays date is: {}".format(date))

def timestamp(request):
    ts = time.time()
    return HttpResponse("Timestamp: {}".format(ts))
         