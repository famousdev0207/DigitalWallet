from dataclasses import fields
from pyexpat import model
from django import forms
from .models import Customer
from .models import Wallet
from .models import Currency
from .models import Account
from .models import Transaction
from .models import Card
from .models import ThirdParty
from .models import Loan
from .models import Reward
from .models import Receipt
from .models import Notification

class CustomerRegistrationForm(forms.ModelForm):
    class Meta:#class inside a class - provides data about a customer
        model = Customer
        fields = '__all__'


class WalletRegistrationForm(forms.ModelForm):
    class Meta:
        model = Wallet
        fields = '__all__'


class CurrencyRegistrationForm(forms.ModelForm):
    class Meta:
        model = Currency
        fields = '__all__'


class AccountRegistrationForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = '__all__'


class TransactionRegistrationForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = '__all__'


class CardRegistrationForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = '__all__'


class ThirdPartyRegistration(forms.ModelForm):
    class Meta:
        model = ThirdParty
        fields = '__all__'

class LoanRegistration(forms.ModelForm):
    class Meta:
        model = Loan
        fields = '__all__'

class ReceiptRegistration(forms.ModelForm):
    class Meta:
        model = Receipt
        fields = '__all__'

class RewardRegistration(forms.ModelForm):
    class Meta:
        model = Reward
        fields = '__all__'


class NotificationRegistration(forms.ModelForm):
    class Meta:
        model = Notification
        fields = '__all__'
