from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.viewsets import ModelViewSet

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
    queryset = Payment.objects.all()
    
    def get_serializer_class(self):
        if self.action == "retrieve":
            return
    