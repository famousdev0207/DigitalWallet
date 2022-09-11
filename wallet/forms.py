from dataclasses import fields
from pyexpat import model
from django import forms
from . import models


class CustomerRegistrationForm(forms.ModelForm):
    class Meta:#class inside a class - provides data about a customer
        model = models.Customer
        fields = ['first_name','last_name','email', 'address', 'phone_number','age','gender']
        widgets = {
            'first_name' : forms.TextInput(attrs = {
                'class': 'form-control',
            }),
             'last_name' : forms.TextInput(attrs = {
                'class': 'form-control',
            }),
             'email' : forms.TextInput(attrs = {
                'class': 'form-control',
            }),
             'address' : forms.TextInput(attrs = {
                'class': 'form-control',
            }),
            'phone_number' : forms.TextInput(attrs = {
                'class': 'form-control',
            }),
            'age' : forms.TextInput(attrs = {
                'class': 'form-control',
            }),
            'gender' : forms.TextInput(attrs = {
                'class': 'form-control',
            }),


        }


class WalletRegistrationForm(forms.ModelForm):
    class Meta:
        model = models.Wallet
        fields = ['balance','customer','amount','currency','history','pin','date_created','status']
        widgets = {
            'balance' : forms.TextInput(attrs = {
                'class': 'form-control',
            }),
             'customer' : forms.TextInput(attrs = {
                'class': 'form-control',
            }),
             'amount' : forms.TextInput(attrs = {
                'class': 'form-control',
            }),
             'currency' : forms.Select(attrs = {
                'class': 'form-control',
            }),
            'history' : forms.TextInput(attrs = {
                'class': 'form-control',
            }),
            'pin' : forms.PasswordInput(attrs = {
                'class': 'form-control',
            }),
            'date_created' : forms.DateTimeInput(attrs = {
                'class': 'form-control',
            }),
            'status' : forms.Select(attrs = {
                'class': 'form-control',
            }),

        }


class CurrencyRegistrationForm(forms.ModelForm):
    class Meta:
        model = models.Currency
        fields = ['country','symbol','amount']
        widgets = {
            'country' : forms.TextInput(attrs = {
                'class': 'form-control',
            }),
             'symbol' : forms.TextInput(attrs = {
                'class': 'form-control',
            }),
             'amount' : forms.TextInput(attrs = {
                'class': 'form-control',
            }),
        }
        


class AccountRegistrationForm(forms.ModelForm):
    class Meta:
        model = models.Account
        fields = ['account_name','account_number','account_type','account_balance','wallet']
        widgets = {
            'account_name' : forms.TextInput(attrs = {
                'class': 'form-control',
            }),
             'account_number' : forms.TextInput(attrs = {
                'class': 'form-control',
            }),
             'account_type' : forms.TextInput(attrs = {
                'class': 'form-control',
            }),
             'account_balance' : forms.TextInput(attrs = {
                'class': 'form-control',
            }),
            'wallet' : forms.TextInput(attrs = {
                'class': 'form-control',
            }),
           
        }


class TransactionRegistrationForm(forms.ModelForm):
    class Meta:
        model = models.Transaction
        fields = ['message','wallet','transaction_description','transaction_amount','transaction_charge','transaction_type','origin_account','destination_account']
        widgets = {
            'message' : forms.TextInput(attrs = {
                'class': 'form-control',
            }),
             'wallet' : forms.TextInput(attrs = {
                'class': 'form-control',
            }),
             'transaction_description' : forms.TextInput(attrs = {
                'class': 'form-control',
            }),
             'transaction_amount' : forms.TextInput(attrs = {
                'class': 'form-control',
            }),
            'transaction_charge' : forms.TextInput(attrs = {
                'class': 'form-control',
            }),
             'transaction_type' : forms.TextInput(attrs = {
                'class': 'form-control',
            }),
             'origin_account' : forms.Select(attrs = {
                'class': 'form-control',
            }),
             'destination_account' : forms.Select(attrs = {
                'class': 'form-control',
            }),
           
        }


class CardRegistrationForm(forms.ModelForm):
    class Meta:
        model = models.Card
        fields = ['card_number','card_type','expiry_date','security_code','date_of_issue','wallet','account','issuer']
        widgets = {
            'card_number' : forms.TextInput(attrs = {
                'class': 'form-control',
            }),
             'card_type' : forms.TextInput(attrs = {
                'class': 'form-control',
            }),
             'expiry_date' : forms.DateTimeInput(attrs = {
                'class': 'form-control',
            }),
             'security_code' : forms.TextInput(attrs = {
                'class': 'form-control',
            }),
            'date_of_issue' : forms.TextInput(attrs = {
                'class': 'form-control',
            }),
             'wallet' : forms.TextInput(attrs = {
                'class': 'form-control',
            }),
             'account' : forms.TextInput(attrs = {
                'class': 'form-control',
            }),
             'issuer' : forms.TextInput(attrs = {
                'class': 'form-control',
            }),
           
        }


class ThirdPartyRegistration(forms.ModelForm):
    class Meta:
        model = models.ThirdParty
        fields = ['account','transaction_amount','currency','date_of_issue','wallet','issuer']
        widgets = {
            'account' : forms.TextInput(attrs = {
                'class': 'form-control',
            }),
             'transaction_amount' : forms.TextInput(attrs = {
                'class': 'form-control',
            }),
             'currency' : forms.Select(attrs = {
                'class': 'form-control',
            }),
             'date_of_issue' : forms.DateTimeInput(attrs = {
                'class': 'form-control',
            }),
             'wallet' : forms.TextInput(attrs = {
                'class': 'form-control',
            }),
             'issuer' : forms.TextInput(attrs = {
                'class': 'form-control',
            }),
           
        }

class LoanRegistration(forms.ModelForm):
    class Meta:
        model = models.Loan
        fields = ['loan_id','loan_type','loan_balance','amount','guaranter','issuer','wallet']
        widgets = {
            'loan_id' : forms.TextInput(attrs = {
                'class': 'form-control',
            }),
             'loan_type' : forms.TextInput(attrs = {
                'class': 'form-control',
            }),
             'loan_balance' : forms.TextInput(attrs = {
                'class': 'form-control',
            }),
             'guaranter' : forms.Select(attrs = {
                'class': 'form-control',
            }),
            'issuer' : forms.Select(attrs = {
                'class': 'form-control',
            }),
            'wallet' : forms.Select(attrs = {
                'class': 'form-control',
            }),
            'amount' : forms.TextInput(attrs = {
                'class': 'form-control',
            }),
           
        }


class ReceiptRegistration(forms.ModelForm):
    class Meta:
        model = models.Receipt
        fields = ['receipt_type','date','receipt_number','amount','transaction','receipt_file']
        widgets = {
            'receipt_type' : forms.TextInput(attrs = {
                'class': 'form-control',
            }),
             'date' : forms.TextInput(attrs = {
                'class': 'form-control',
            }),
             'receipt_number' : forms.TextInput(attrs = {
                'class': 'form-control',
            }),
             'amount' : forms.TextInput(attrs = {
                'class': 'form-control',
            }),
            'transaction' : forms.Select(attrs = {
                'class': 'form-control',
            }),
            'receipt_file' : forms.FileInput(attrs = {
                'class': 'form-control',
            }),
           
        }


class RewardRegistration(forms.ModelForm):
    class Meta:
        model = models.Reward
        fields = ['transaction','recipient','date_of_reward','points']
        widgets = {
            'transaction' : forms.TextInput(attrs = {
                'class': 'form-control',
            }),
             'recipient' : forms.TextInput(attrs = {
                'class': 'form-control',
            }),
             'date_of_reward' : forms.DateTimeInput(attrs = {
                'class': 'form-control',
            }),
            'points' : forms.DateTimeInput(attrs = {
                'class': 'form-control',
            }),
        }


class NotificationRegistration(forms.ModelForm):
    class Meta:
        model = models.Notification
        fields = ['message','date','recipient','title']
        widgets = {
            'message' : forms.TextInput(attrs = {
                'class': 'form-control',
            }),
             'date' : forms.DateTimeInput(attrs = {
                'class': 'form-control',
            }),
             'recipient' : forms.TextInput(attrs = {
                'class': 'form-control',
            }),
             'title' : forms.TextInput(attrs = {
                'class': 'form-control',
            }),
        }

