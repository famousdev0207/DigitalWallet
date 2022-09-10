from django.urls import path
from . import views
urlpatterns = [
    path('register/', views.register_customer, name='registration'),
    path('create/', views.create_wallet, name='create'),
    path('currency/', views.register_currency, name='currencyForm'),
    path('account/', views.register_account, name='account'),
    path('transaction/',views.register_transaction, name = 'transaction'),
    path('cards/', views.register_card, name = 'cards'),
    path('thirdparty/',views.register_thirdparty, name = 'thirdparty'),
    path('reward/', views.register_reward, name='reward'),
    path('loan/', views.register_loan, name = 'loan'),
    path('notification/', views.register_notification, name = 'notification'),
    path('receipt/', views.register_receipt, name = 'receipt'),
    # displaying list of objects in wallet
    path('customers/', views.list_customers, name = 'customers'),
    path('accounts/', views.list_accounts, name = 'accounts'),
    path('transactions/', views.list_transactions, name = 'transactions'),
    path('notifications/', views.list_notifications, name = 'notifications'),
    path('receipts/', views.list_receipts, name = 'receipts'),
    path('listcards/', views.list_cards, name = 'listcards'),
    path('wallets/', views.list_wallets, name = 'wallets'),
    path('loans/', views.list_loans, name = 'loan'),
    path('rewards/', views.list_rewards, name = 'rewards'),
    path('thirdpartys/', views.list_thirdparty, name = 'thirdpartys'),
    path('currencies/', views.list_currency, name = 'currency'),

]