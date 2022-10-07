from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from  wallet.models import Customer,Wallet,Account,Card,Transaction,Loan,Receipt,Notification


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('first_name', 'last_name', 'email', 'age', 'address', 'phone_number', 'gender')

class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields =('customer','balance','amount','date_created','status','history','pin')

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields =('account_name','account_number','account_type','account_balance','wallet')

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ('card_number','card_type','card_number','expiry_date','account','issuer')

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('message','wallet','transaction_description','transaction_amount','transaction_charge','transaction_type','origin_account','destination_account')

class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields =('loan_id','loan_type','loan_balance','amount','guaranter','issuer','wallet')

class ReceiptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receipt
        fields = ('receipt_type','date','receipt_number','amount','transaction','receipt_file')

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ('message','date','recipient','title')





