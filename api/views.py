from operator import and_
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import views
from rest_framework.response import Response
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


class AccountDepositView(views.APIView):
   """
   This class allows deposit of funds to an account.
   Accepts this JSON data
   {
       "account_id": 123,
       "amount": 1000
   }
   This API needs Authentication and Permissions to be added
   """
   def post(self, request, format=None):       
       account_id = request.data["account_id"]
       amount = request.data["amount"]
       try:
           account = Account.objects.get(id=account_id)
       except ObjectDoesNotExist:
           return Response("Account Not Found", status=404)
      
       message, status = account.deposit(amount)
       return Response(message, status=status)

   def get(self,request,id,format=None):
    account_id = Account.objects.get(id=id)
    if request.method == 'GET':
        serializer_account = serializers.AccountSerializer(account_id)
        return Response(serializer_account.data)



class AccountTransferView(views.APIView):
    def post(self, request, id, format=None):       
       account_id = request.data["destination_account"]
       amount = request.data["amount"]
       origin_account = Account.objects.get(id = id)
       try:
           account = Account.objects.get(id= account_id)
       except ObjectDoesNotExist:
           return Response("Account Not Found", status=404)
      
       message, status = origin_account.transfer(account,amount)
       return Response(message, status=status)


class AccountLoanRequestView(views.APIView):
    def post(self,request,format=None):
        account_id=request.data["account_id"]
        amount=request.data["amount"]
        try:
            account=Account.objects.get(id=account_id)    
        except ObjectDoesNotExist:  #whenn no object exist
            return Response("Account Not Found", status=404)
        message, status = account.borrow(amount) 
        return Response (message,status=status)


class AccountLoanRepaymentView(views.APIView):
    def post(self,request,format=None):
        account_id=request.data["account_id"]
        amount=request.data["amount"]
        try:
            account=Account.objects.get(id=account_id)    
        except ObjectDoesNotExist:  #whenn no object exist
            return Response("Account Not Found", status=404)
        message, status = account.loan_repayment(amount) 
        return Response (message,status=status)

class AccountWithdrawalView(views.APIView):
    def post(self,request,pk,format=None):
        account_id=request.data["account_id"]    #creating account id 
        amount=request.data["amount"]
        try:
            account=Account.objects.get(id=account_id)    
        except ObjectDoesNotExist:  #whenn no object exist
            return Response("Account Not Found", status=404)
        message, status = account.withdraw(amount) 
        return Response (message,status=status)




