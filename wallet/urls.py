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
    path('customers/<int:id>/', views.customer_profile, name = 'customer_profile'),
    path('customers/edit/<int:id>', views.edit_customer, name = 'edit_customer'),
    path('getwallet/<int:id>/', views.wallet_profile, name = 'wallet_profile'),
    path('wallets/edit/<int:id>', views.edit_wallet, name = 'edit_wallet'),
    path('account-profile/<int:id>/', views.account_profile, name = 'account_profile'),
    path('accounts/edit/<int:id>', views.edit_account, name = 'edit_account'),
    path('cards/<int:id>/', views.card_profile, name = 'card_profile'),
    path('cards/edit/<int:id>', views.edit_card, name = 'edit_card'),
    path('transaction/<int:id>/', views.transaction_profile, name = 'transaction_profile'),
    path('transaction/edit/<int:id>', views.edit_transaction, name = 'edit_transaction'),
    path('receipt/<int:id>/',views.receipt_profile, name = 'receipt_profile'),
    path('receipt/edit/<int:id>', views.edit_receipt, name = 'edit_receipt')



]