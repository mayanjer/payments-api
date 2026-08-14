from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound
from .models import *
from .serializers import *
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
import json

# Create your views here.

class PayerViewSet(ModelViewSet):
    
    queryset = Payer.objects.all()
    
    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return PayerSerializerGet
        elif self.action == "create":
            return PayerSerializer
        # return super().get_serializer_class()
    
class PayeeViewSet(ModelViewSet):
    
    queryset = Payee.objects.all()
      
    def get_serializer_class(self):
        if self.action == 'create':
            self.serializer_class = PayeeSerializer 
        elif self.action in ["retrieve", "list"]:
            return PayeeSerializerGet
        return super().get_serializer_class()
    
class PaymentViewSet(ModelViewSet):
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["payment_status"]
    try:
        queryset = Payment.objects.all()
    except Payment.DoesNotExist:
        raise NotFound({"error_code": "payment not found"})
    
    def get_serializer_class(self):
        if self.action == "retrieve":
            return PaymentSerializerRetrieve
        return PaymentSerializer
    
    def create(self, request, *args, **kwargs):
        payload = request.data.copy() #the reson we use copy is because by default data from forms is parsed to a Querydict which is immutable. It only allows mutation with data from JSON objects becuase the data is parsed to normal python dictionaries
        if payload.get("payment_status") == None:
            payload["payment_status"] = "PENDING"
        serializer = self.get_serializer(data = payload)
        serializer.is_valid(raise_exception = True)
        self.perform_create(serializer)
        
        headers = self.get_success_headers(serializer.data)
        return super().create(request, *args, **kwargs)