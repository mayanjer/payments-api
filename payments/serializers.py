from rest_framework.serializers import ModelSerializer
from .models import *

# payer serializers
class PayerSerializer(ModelSerializer):  
    class Meta:
        model = Payer
        fields = ("first_name", "last_name")    
class PayerSerializerGet(ModelSerializer):
    class Meta:
        model = Payer
        fields = ("__all__")

    # Payee serializers
class PayeeSerializer(ModelSerializer):
    class Meta:
        model = Payee
        fields = ("first_name", "last_name") 
class PayeeSerializerGet(ModelSerializer):
    class Meta:
        model = Payee
        fields = ("__all__")
        
# payment serializers
class PaymentSerializer(ModelSerializer):
    class Meta:
        model = Payment
        fields = ("__all__")
class PaymentSerializerRetrieve(ModelSerializer):
    class Meta:
        model = Payment
        fields = ("")