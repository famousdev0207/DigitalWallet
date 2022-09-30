from locale import currency
from django.shortcuts import render,redirect
from . import forms
from . import models
#content of http request
# Create your views here.

def register_customer(request):
    if request.method == 'POST':
        form = forms.CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
      form = forms.CustomerRegistrationForm() #instance of CustomerRegistrationForm
    return render(request, "wallet/register_customer.html",
    {'form': form})

def create_wallet(request):
    if request.method == 'POST':
        form = forms.WalletRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
     form  = forms.WalletRegistrationForm() #instance of WalletRegistrationForm    
    return render(request, "wallet/create_wallet.html", 
    {'form': form})


def register_currency(request):
    if request.method == 'POST':
        form = forms.CurrencyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
     form = forms.CurrencyRegistrationForm() #instance of CurrencyRegistrationForm
    return render(request, "wallet/register_currency.html",
    {'form': form})


def register_account(request):
    if request.method == 'POST':
        form = forms.AccountRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
     form = forms.AccountRegistrationForm() #instance of AccountRegistrationForm
    return render(request, "wallet/register_account.html",
    {'form': form})


def register_transaction(request):
    if request.method == 'POST':
        form = forms.TransactionRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
     form = forms.TransactionRegistrationForm() #instance of TransactionRegistrationForm
    return render(request, "wallet/register_transaction.html",
    {'form': form})


def register_card(request):
    if request.method == 'POST':
        form = forms.CardRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
     form = forms.CardRegistrationForm() #instance of CardRegistrationForm
    return render(request, "wallet/register_cards.html",
    {'form': form})

def register_thirdparty(request):
    if request.method == 'POST':
        form = forms.ThirdPartyRegistration(request.POST)
        if form.is_valid():
            form.save()
    else:
     form = forms.ThirdPartyRegistration() #instance of ThirdPartyRegistrationForm
    return render(request, "wallet/register_thirdparty.html",
    {'form': form})

def register_notification (request):
    if request.method == 'POST':
        form = forms.NotificationRegistration(request.POST)
        if form.is_valid():
            form.save()
    else:
     form = forms.NotificationRegistration() #instance of NotificationRegistrationForm
    return render(request, "wallet/register_notification.html",
    {'form': form})

def register_loan (request):
    if request.method == 'POST':
        form = forms.LoanRegistration(request.POST)
        if form.is_valid():
            form.save()
    else:
     form = forms.LoanRegistration() #instance of LoanRegistrationForm
    return render(request, "wallet/register_loan.html",
    {'form': form}) 

def register_reward (request):
    if request.method == 'POST':
        form = forms.RewardRegistration(request.POST)
        if form.is_valid():
            form.save()
    else:
     form = forms.RewardRegistration()#instance of LoanRegistrationForm
    return render(request, "wallet/register_reward.html",
    {'form': form})

def register_receipt (request):
    if request.method == 'POST':
        form = forms.ReceiptRegistration(request.POST)
        if form.is_valid():
            form.save()
    else:
     form = forms.ReceiptRegistration() #instance of ReceiptRegistration
    return render(request, "wallet/register_receipt.html",
    {'form': form}) 

def list_customers(request):
    customers = models.Customer.objects.all()
    return render(request, "wallet/list_customers.html",
    {'customers': customers})

def list_accounts(request):
    accounts = models.Account.objects.all()
    return render(request, "wallet/accounts.html", 
    {'accounts': accounts})

def list_wallets(request):
    wallets = models.Wallet.objects.all()
    return render(request, "wallet/list_wallets.html",
    {'wallets': wallets})

def list_transactions(request):
    transactions = models.Transaction.objects.all()
    return render(request, "wallet/list_transactions.html",
    {'transactions': transactions})

def list_currency(request):
    currencys = models.Currency.objects.all()
    return render(request, 'wallet/list_currencies.html', 
    {'currencys': currencys})

def list_receipts(request):
    receipts = models.Receipt.objects.all()
    return render(request, "wallet/list_receipts.html",
    {'receipts': receipts})
    

def list_cards(request):
    cards = models.Card.objects.all()
    return render(request, "wallet/list_cards.html",
    {'cards': cards})

def list_loans(request):
    loans = models.Loan.objects.all()
    return render(request, "wallet/list_loans.html",
    {'loans': loans})

def list_rewards(request):
    rewards = models.Reward.objects.all()
    return render(request, "wallet/list_rewards.html",
    {'rewards': rewards})


def list_thirdparty(request):
    thirdparties = models.ThirdParty.objects.all()
    return render(request, "wallet/list_third_party.html",
    {'thirdparties': thirdparties})

def list_notifications(request):
    notifications = models.Notification.objects.all()
    return render(request, 'wallet/list_notifications.html',
    {'notifications': notifications})


def customer_profile (request,id):
    customer = models.Customer.objects.get(id=id)
    return render(request, 'wallet/customer_profile.html', 
    {"customer": customer})

def edit_customer(request, id):
    customer = models.Customer.objects.get(id=id)
    if request.method == 'POST':
        form = forms.CustomerRegistrationForm(request.POST,
        instance=customer)
        if form.is_valid():
            form.save()
            return redirect ('customer_profile', id= customer.id)
    else:
        form = forms.CustomerRegistrationForm(instance=customer)
        return render(request, 'wallet/edit_customer.html', 
        {'form': form})


def wallet_profile (request,id):
    wallet = models.Wallet.objects.get(id=id)
    return render(request, 'wallet/wallet_profile.html', 
    {"wallet": wallet})

def edit_wallet(request, id):
    wallet = models.Wallet.objects.get(id=id)
    if request.method == 'POST':
        form = forms.WalletRegistrationForm(request.POST,
        instance=wallet)
        if form.is_valid():
            form.save()
            return redirect ('wallet_profile', id= wallet.id)
    else:
        form = forms.WalletRegistrationForm(instance=wallet)
        return render(request, 'wallet/edit_wallet.html', 
        {'form': form})

def account_profile (request,id):
    account = models.Account.objects.get(id=id)
    return render(request, 'wallet/account_profile.html', 
    {"account": account})

def edit_account(request, id):
    account = models.Account.objects.get(id=id)
    if request.method == 'POST':
        form = forms.AccountRegistrationForm(request.POST,
        instance=account)
        if form.is_valid():
            form.save()
            return redirect ('account_profile', id= account.id)
    else:
        form = forms.WalletRegistrationForm(instance=account)
        return render(request, 'wallet/edit_account.html', 
        {'form': form})







