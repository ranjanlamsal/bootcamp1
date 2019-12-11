from django.contrib import admin
from django.urls import path
from timeteller.views import home
from timeteller.views import today , timestamp


urlpatterns = [

    path('', home),
    path('today/', today),
    path('timestamp/', timestamp),
]