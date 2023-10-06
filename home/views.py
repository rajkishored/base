from django.shortcuts import render
from .serializer import mytable,myaddress,myemployee,myemployer
from rest_framework.generics import CreateAPIView,ListAPIView, ListCreateAPIView
from .models import Job,Employee,Employer,Address


class mycreate(CreateAPIView):
    queryset=Job
    
    querryset=Employer
    querryset=Address
    serializer_class=mytable


class myvie(ListAPIView):
    queryset=Job.objects.all()
    serializer_class=mytable



class myempcreate(ListCreateAPIView):
    queryset=Employee.objects.all()
    serializer_class=myemployee

class myemplercreate(ListCreateAPIView):
    queryset=Employer.objects.all()
    serializer_class=myemployer

class myedresscreate(ListCreateAPIView):
     queryset=Address.objects.all()
     serializer_class=myaddress
# Create your views here.
