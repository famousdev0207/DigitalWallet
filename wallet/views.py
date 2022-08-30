from django.shortcuts import render
from .forms import CustomerRegistrationForm
from .forms import  WalletRegistrationForm
from .forms import  CurrencyRegistrationForm
from .forms import  AccountRegistrationForm
from .forms import TransactionRegistrationForm
from .forms import CardRegistrationForm
from .forms import  ThirdPartyRegistration
from .forms import  ReceiptRegistration
from .forms import  NotificationRegistration
from .forms import RewardRegistration
from .forms import NotificationRegistration
from .forms import LoanRegistration

#content of http request
# Create your views here.

def register_customer(request):
    form = CustomerRegistrationForm() #instance of CustomerRegistrationForm
    return render(request, "wallet/register_customer.html",
    {'form': form})

def create_wallet(request):
    form  = WalletRegistrationForm() #instance of WalletRegistrationForm    
    return render(request, "wallet/create_wallet.html", 
    {'form': form})


def register_currency(request):
    form = CurrencyRegistrationForm() #instance of CurrencyRegistrationForm
    return render(request, "wallet/register_currency.html",
    {'form': form})


def register_account(request):
    form = AccountRegistrationForm() #instance of AccountRegistrationForm
    return render(request, "wallet/register_account.html",
    {'form': form})


def register_transaction(request):
    form = TransactionRegistrationForm() #instance of TransactionRegistrationForm
    return render(request, "wallet/register_transaction.html",
    {'form': form})


def register_card(request):
    form = CardRegistrationForm() #instance of CardRegistrationForm
    return render(request, "wallet/register_cards.html",
    {'form': form})

def register_thirdparty(request):
    form = ThirdPartyRegistration() #instance of ThirdPartyRegistrationForm
    return render(request, "wallet/register_thirdparty.html",
    {'form': form})

def register_notification (request):
    form = NotificationRegistration() #instance of NotificationRegistrationForm
    return render(request, "wallet/register_notification.html",
    {'form': form})

def register_loan (request):
    form = LoanRegistration() #instance of LoanRegistrationForm
    return render(request, "wallet/register_loan.html",
    {'form': form}) 

def register_reward (request):
    form = RewardRegistration()#instance of LoanRegistrationForm
    return render(request, "wallet/register_reward.html",
    {'form': form})

def register_receipt (request):
    form = ReceiptRegistration() #instance of ReceiptRegistration
    return render(request, "wallet/register_receipt.html",
    {'form': form}) 



