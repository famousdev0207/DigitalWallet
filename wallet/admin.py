from django.contrib import admin
from .models import Customer
from .models import Wallet
from .models import Account
from .models import Transaction
from .models import Card
from .models import ThirdParty
from .models import Receipt
from .models import Loan
from .models import Reward
from .models import Notification
from .models import Currency

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'age', 'email')
    search_fields = ('first_name', 'last_name')
admin.site.register(Customer, CustomerAdmin)

class AccountAdmin(admin.ModelAdmin):
    list_display = ('account_name', 'account_number', 'wallet')
    search_fields = ('account_name', 'account_number')
admin.site.register(Account, AccountAdmin)
class WalletAdmin(admin.ModelAdmin):
    list_display = ('customer','currency','amount','date_created')
    search_fields = ('customer','amount','date_created')
admin.site.register( Wallet, WalletAdmin)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('wallet', 'transaction_amount','transaction_description','origin_account','destination_account')
    search_fields = ('wallet','transaction_amount','transaction_description','origin_account','destination_account')
admin.site.register(Transaction, TransactionAdmin)
class CardAdmin(admin.ModelAdmin):
    list_display = ('card_type','card_number','wallet')
    search_fields = ('card_type','card_number','wallet')
admin.site.register(Card, CardAdmin) 
class ThirdPartyAdmin(admin.ModelAdmin):
    list_display = ('account','wallet', 'issuer', 'currency')
    search_fields = ('account','wallet', 'issuer', 'currency')
admin.site.register(ThirdParty, ThirdPartyAdmin)
class ReceiptAdmin(admin.ModelAdmin):
    list_display = ('transaction', 'receipt_type','amount','receipt_number')
    search_fields = ('transaction', 'amount', 'receipt_number')
admin.site.register(Receipt, ReceiptAdmin)
class LoanAdmin(admin.ModelAdmin):
    list_display = ('guaranter','issuer','wallet', 'loan_type')
    search_fields = ('guaranter','issuer','wallet', 'loan_type')
admin.site.register(Loan,LoanAdmin)
class ReceiptAdmin(admin.ModelAdmin):
    list_display = ('transaction', 'recipient', 'date_of_reward')
    search_fields = ('recipient', 'transaction','date_of_reward')
admin.site.register(Reward, ReceiptAdmin)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('message','date','recipient')
    search_fields = ('message','date','recipient')
admin.site.register(Notification, NotificationAdmin)
class CurrencyAdmin(admin.ModelAdmin):
    list_display  = ('country', 'amount', 'symbol')
    search_fields = ('country', 'amount', 'symbol')
admin.site.register(Currency, CurrencyAdmin)