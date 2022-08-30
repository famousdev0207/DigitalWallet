from django.urls import path
from .views import register_customer
from .views import create_wallet
from .views import register_currency
from .views import register_account
from .views import register_transaction
from .views import register_card
from .views import register_thirdparty
from .views import register_reward
from .views import register_loan
from .views import register_notification
from .views import register_receipt
urlpatterns = [
    path('register/', register_customer, name='registration'),
    path('create/', create_wallet, name='create'),
    path('currency/', register_currency, name='currencyForm'),
    path('account/', register_account, name='account'),
    path('transaction/',register_transaction, name = 'transaction'),
    path('cards/', register_card, name = 'cards'),
    path('thirdparty/',register_thirdparty, name = 'thirdparty'),
    path('reward/', register_reward, name='reward'),
    path('loan/', register_loan, name = 'loan'),
    path('notification/', register_notification, name = 'notification'),
    path('receipt/', register_receipt, name = 'receipt'),

]