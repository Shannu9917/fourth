from django.urls import path
from app5.views import *

app_name='neku adee '
urlpatterns=[
    path('neku/',neku,name='neku'),
]
