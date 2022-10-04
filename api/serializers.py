from pyexpat import model
from rest_framework import serializers
from  wallet.models import Customer,Wallet


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('first_name', 'last_name', 'email', 'age', 'address', 'phone_number', 'gender')

class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields =('customer','balance','amount',)