#connect view ----> url
from django.urls import path

from .views import hello, stdlist, second, hi, newlist

urlpatterns = [
    path('hello/', hello, name = 'hello'),
    path('hi', hi),
    path('list', stdlist),
    path('second', second),
    path('newlist', newlist)


]