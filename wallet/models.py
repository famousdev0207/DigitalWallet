from django.db import models

# Create your models here.
class Customer(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    address=models.CharField(max_length=20)
    email=models.EmailField(max_length=254)
    phone_number=models.CharField(max_length=13)
    GENDER_CHOICES = (
           ("M", "Male"),
           ("F", "Female"),
           ("NB", "Non-Binary"),
    )
    gender=models.CharField(max_length=10, choices= GENDER_CHOICES)
    age=models.PositiveSmallIntegerField()
    profile_picture = models.ImageField(default='default.jpg', upload_to='profile_pics')
    def __str__(self):
        return '{} by {}'.format(self.first_name, self.last_name,self.address,self.email,self.phone_number,self.gender,self.age,self.profile_picture)


class Currency(models.Model):
    country= models.CharField(max_length=30)
    symbol= models.CharField(max_length=5)
    amount= models.BigIntegerField()
    def __str__(self):
        return '{} {}'.format(self.country, self.symbol, self.amount)


class Wallet(models.Model):
    balance = models.IntegerField()
    customer = models.ForeignKey("Customer",on_delete=models.CASCADE,related_name='Wallet_customer')
    amount  = models.IntegerField()
    date_created = models.DateTimeField()
    status = models.CharField(max_length=15)
    currency = models.ForeignKey("Currency",on_delete=models.CASCADE,related_name='Wallet_currency')
    history = models.DateTimeField()
    pin = models.IntegerField()
    def __str__(self):
        return '{} {}'.format(self.balance,self.currency,self.customer.first_name , self.status)

class Account(models.Model):
    account_name = models.CharField(max_length=20)
    account_number = models.IntegerField()
    account_type = models.CharField(max_length=20)
    account_balance = models.IntegerField()
    wallet = models.ForeignKey("Wallet",on_delete=models.CASCADE,related_name='Account_wallet')
    def __str__(self):
        return'{}{}'.format(self.account_balance,self.account_number,self.account_type,self.wallet.customer.first_name)


class Transaction(models.Model):
    message = models.CharField(max_length=100)
    wallet = models.ForeignKey("Wallet",on_delete=models.CASCADE,related_name='Transaction_wallet')
    transaction_description = models.CharField(max_length=9)
    transaction_amount = models.BigIntegerField()
    transaction_charge = models.IntegerField()
    transaction_type = models.CharField(max_length=6)
    origin_account = models.ForeignKey("Wallet", on_delete=models.CASCADE,related_name='Transaction_origin')
    destination_account = models.ForeignKey("Wallet", on_delete=models.CASCADE,related_name='Transaction_destination')
    def __str__(self):
        return '{}{}'.format(self.message, self.destination_account,self.origin_account,self.transaction_amount,self.wallet.customer.first_name)


class Card(models.Model):
    card_number= models.IntegerField()
    card_type= models.CharField(max_length=20)
    expiry_date = models.DateField()
    security_code = models.IntegerField()
    date_of_issue = models.DateTimeField()
    wallet= models.ForeignKey("Wallet",on_delete=models.CASCADE,related_name='Card_wallet')
    account= models.ForeignKey("Account",on_delete=models.CASCADE,related_name='Card_account')
    issuer= models.CharField(max_length=10)

    def __str__(self):
        return '{} {}'.format(self.card_number,self.card_type,self.expiry_date,self.wallet.customer.first_name,self.account.account_name, self.issuer)


class ThirdParty(models.Model):
    account= models.ForeignKey("Account",on_delete=models.CASCADE,related_name='Thirdparty_account')
    transaction_amount= models.BigIntegerField()
    currency = models.ForeignKey("Currency",on_delete=models.CASCADE,related_name='Thirdparty_currency')
    date_of_issue = models.DateTimeField()
    wallet= models.ForeignKey("Wallet",on_delete=models.CASCADE,related_name='Thirdparty_wallet')
    issuer= models.CharField(max_length=20)
    def __str__(self):
        return'{} {}'.format(self.account.account_name, self.transaction_amount,self.wallet.name)


class Notification(models.Model):
    message= models.CharField(max_length=100)
    date = models.DateTimeField()
    recipient= models.ForeignKey("Customer",on_delete=models.CASCADE,related_name='Thirdparty_recipient')
    title = models.CharField(max_length=20)
    def __str__(self):
        return'{} {}'.format(self.message, self.recipient,self.title)


class Receipt(models.Model):
    receipt_type= models.CharField(max_length = 20)
    date = models.DateTimeField()
    receipt_number= models.IntegerField()
    amount= models.IntegerField()
    transaction = models.ForeignKey("Transaction",on_delete=models.CASCADE,related_name='Thirdparty_transaction')
    receipt_file = models.FileField()
    def __str__(self):
        return '{} {}'.format(self.receipt_file,self.amount,self.transaction.amount,self.receipt_file)


class Loan(models.Model):
    loan_id = models.IntegerField()
    loan_type = models.CharField(max_length=15)
    loan_balance = models.IntegerField()
    amount = models.IntegerField()
    guaranter = models.CharField(max_length=20)
    issuer = models.CharField(max_length=20)
    wallet = models.ForeignKey("Wallet",on_delete=models.CASCADE,related_name='Loan_wallet')

    def __str__(self):
        return '{}{}'.format(self.loan_balance,self.loan_id,self.amount,self.guaranter,self.wallet.name)


class Reward(models.Model):
    transaction= models.ForeignKey("Transaction",on_delete=models.CASCADE,related_name='Reward_transaction')
    recipient = models.ForeignKey("Customer",on_delete=models.CASCADE,related_name='Reward_recipient')
    date_of_reward = models.DateTimeField()
    points = models.IntegerField()
    def __str__(self):
        return '{}{}'.format(self.transaction,self.recipient,self.date_of_reward,self.points)





    






