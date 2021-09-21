from django.shortcuts import render
from core.models import FillNumbers, CoderHome
from django.http import HttpResponse
from rest_framework import viewsets       
from .serializers import FillSerializer, CoderHomeSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
# Create your views here.

def listing(request):
    return HttpResponse('This is the listing page')

        
class FillView(viewsets.ModelViewSet): 
  serializer_class = FillSerializer      
  queryset = FillNumbers.objects.all()
  http_method_names = ['get', 'post', 'put', 'patch', 'delete']
       
    # def get_queryset(self):
    #     return self.queryset.filter(user=self.request.user) 

  def destroy(self, request, *args, **kwargs):
    instance = self.get_object()
    self.perform_destroy(instance)
    return Response(status=status.HTTP_204_NO_CONTENT)

class CoderView(viewsets.ModelViewSet):
  serializer_class = CoderHomeSerializer
  queryset = CoderHome.objects.all()
  permission_classes = (IsAuthenticated,)
  http_method_names = ['get', 'post', 'patch', 'put', 'delete']

  def destroy(self, request, *args, **kwargs):
    instance = self.get_object()
    self.perform_destroy(instance)
    return Response(status=status.HTTP_204_NO_CONTENT)