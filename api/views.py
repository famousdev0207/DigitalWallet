from django.shortcuts import render
from rest_framework import viewsets
from wallet.models import Customer,Wallet,Account,Card,Transaction,Loan,Receipt,Notification
from . import serializers
# Create your views here.

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = serializers.CustomerSerializer


class WalletViewSet(viewsets.ModelViewSet):
    queryset = Wallet.objects.all()
    serializer_class = serializers.WalletSerializer


class  AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = serializers.AccountSerializer


class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = serializers.CardSerializer


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = serializers.TransactionSerializer

class LoanViewSet(viewsets.ModelViewSet):
    queryset = Loan.objects.all()
    serializer_class = serializers.LoanSerializer

class ReceiptViewSet(viewsets.ModelViewSet):
    queryset = Receipt.objects.all()
    serializer_class = serializers.ReceiptSerializer

class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = serializers.NotificationSerializer





