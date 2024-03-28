from django.shortcuts import render
from django.http import HttpResponse 

from rest_framework.response import Response

from rest_framework import viewsets
from rest_framework.decorators import api_view

from .models import PhoneData
from .serializer import ComparisonSerializer

from rest_framework import mixins
from rest_framework import generics

def index(request):
    phone_data = PhoneData.objects.all()
    return render(request, 'index.html', {'phone_data': phone_data})


class model_view(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    
    serializer_class = ComparisonSerializer
    queryset = PhoneData.objects.all()

    def get(self, request, *args, **kwargs):
        
        return self.list(request, *args, **kwargs)