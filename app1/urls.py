from django.urls import path
from app1.views import *

app_name=('madhu')

urlpatterns=[

    path('specific1/',specific1,name='specific1'),
    path('specific2/',specific2,name='specific2'),
]