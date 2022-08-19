# Generated by Django 4.0.6 on 2022-08-19 14:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_name', models.CharField(max_length=20)),
                ('account_number', models.IntegerField()),
                ('account_type', models.CharField(max_length=20)),
                ('account_balance', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=30)),
                ('symbol', models.CharField(max_length=5)),
                ('amount', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('address', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=13)),
                ('gender', models.CharField(max_length=10)),
                ('age', models.PositiveSmallIntegerField()),
                ('profile_picture', models.ImageField(default='default.jpg', upload_to='profile_pics')),
            ],
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.IntegerField()),
                ('amount', models.IntegerField()),
                ('date_created', models.DateTimeField()),
                ('status', models.CharField(max_length=15)),
                ('history', models.DateTimeField()),
                ('pin', models.IntegerField()),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Wallet_currency', to='wallet.currency')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Wallet_customer', to='wallet.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=100)),
                ('transaction_description', models.CharField(max_length=9)),
                ('transaction_amount', models.BigIntegerField()),
                ('transaction_charge', models.IntegerField()),
                ('transaction_type', models.CharField(max_length=6)),
                ('destination_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Transaction_destination', to='wallet.wallet')),
                ('origin_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Transaction_origin', to='wallet.wallet')),
                ('wallet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Transaction_wallet', to='wallet.wallet')),
            ],
        ),
        migrations.CreateModel(
            name='ThirdParty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_amount', models.BigIntegerField()),
                ('date_of_issue', models.DateTimeField()),
                ('issuer', models.CharField(max_length=20)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Thirdparty_account', to='wallet.account')),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Thirdparty_currency', to='wallet.currency')),
                ('wallet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Thirdparty_wallet', to='wallet.wallet')),
            ],
        ),
        migrations.CreateModel(
            name='Reward',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_reward', models.DateTimeField()),
                ('points', models.IntegerField()),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Reward_recipient', to='wallet.customer')),
                ('transaction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Reward_transaction', to='wallet.transaction')),
            ],
        ),
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receipt_type', models.CharField(max_length=20)),
                ('date', models.DateTimeField()),
                ('receipt_number', models.IntegerField()),
                ('amount', models.IntegerField()),
                ('receipt_file', models.FileField(upload_to='')),
                ('transaction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Thirdparty_transaction', to='wallet.transaction')),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=100)),
                ('date', models.DateTimeField()),
                ('title', models.CharField(max_length=20)),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Thirdparty_recipient', to='wallet.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loan_id', models.IntegerField()),
                ('loan_type', models.CharField(max_length=15)),
                ('loan_balance', models.IntegerField()),
                ('amount', models.IntegerField()),
                ('guaranter', models.CharField(max_length=20)),
                ('issuer', models.CharField(max_length=20)),
                ('wallet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Loan_wallet', to='wallet.wallet')),
            ],
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_number', models.IntegerField()),
                ('card_type', models.CharField(max_length=20)),
                ('expiry_date', models.DateField()),
                ('security_code', models.IntegerField()),
                ('date_of_issue', models.DateTimeField()),
                ('issuer', models.CharField(max_length=10)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Card_account', to='wallet.account')),
                ('wallet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Card_wallet', to='wallet.wallet')),
            ],
        ),
        migrations.AddField(
            model_name='account',
            name='wallet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Account_wallet', to='wallet.wallet'),
        ),
    ]
