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

admin.site.register(Customer,CustomerAdmin)
admin.site.register( Wallet)
admin.site.register(Account)
admin.site.register(Transaction)
admin.site.register(Card) 
admin.site.register(ThirdParty)
admin.site.register(Receipt)
admin.site.register(Loan)
admin.site.register(Reward)
admin.site.register(Notification)
admin.site.register(Currency)