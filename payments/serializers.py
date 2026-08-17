from rest_framework.serializers import ModelSerializer
from .models import *

# payer serializers
class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "username")

class PayerSerializer(ModelSerializer):  
    class Meta:
        model = Payer
        fields = ("user__first_name", "user__last_name", "user__user_name")    
class PayerSerializerGet(ModelSerializer):
    class Meta:
        model = Payer
        fields = ("__all__")

    # Payee serializers
class PayeeSerializer(ModelSerializer):
    class Meta:
        model = Payee
        fields = ("user__first_name", "user__last_name", "user_name") 
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
    payer = PayerSerializer(read_only=True)
    payee = PayeeSerializer(read_only=True)
    class Meta:
        model = Payment
        fields = ("__all__")