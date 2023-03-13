from django.urls import path
from ENGLAND.views import *
app_name='nothing'

urlpatterns=[
    path('Eng/',Eng,name='Eng'),
]