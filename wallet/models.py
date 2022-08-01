# from distutils.command.upload import upload
from datetime import datetime
import email
# from email.headerregistry import Address
from email.policy import default
from locale import currency
# from tkinter import CASCADE
from django.db import models



class Customer(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    address = models.TextField(max_length=13)
    email = models.EmailField()
    phone_number = models.CharField(max_length=13)
    gender = models.CharField(max_length=8)
    age = models.PositiveSmallIntegerField()
    password = models.CharField(max_length=8)
    nationality = models.CharField(max_length=2)
    profile_picture = models.ImageField(default='default.jpg',upload_to='profile pics')
    employment=models.BooleanField()

class Wallet(models.Model):
    currency = models.CharField(max_length= 30)
    amount = models.IntegerField()  
    Customers_id = models.ForeignKey('Customer', on_delete= models.CASCADE)  
    balance = models.IntegerField()
    date = models.DateTimeField()
    status = models.CharField(max_length=200)
    pin = models.TextField(max_length=12,default="")
    history = models.DateTimeField()
    # transactions = models.ForeignKey('Transaction',on_delete=models.CASCADE)


class Account(models.Model): 
    account_number = models.IntegerField() 
    account_type = models.CharField()
    balance = models.IntegerField()
    name = models.CharField ( 'Customer', on_delete= models.CASCADE)
    Wallet = models.ForeignKey()

class Transaction(models.model):
     transaction =models.CharField()
     wallet = models.ForeignKey()
     transaction_number = models.CharField()
     transaction_amount = models.BigAutoField()
     transaction_type = models.CharField()
     transaction_charge = models.IntegerField()
     datetime = models.DateTimeField()
     receipt = models.ForeignKey()
     origin_account = models.ForeignKey()
     destination_account = models.ForeignKey()

class Card (models.model):
    user_card_number = models.BigAutoField()
    pin = models.CharField()
    debit_card = models.CharField()
    credit_card = models.CharField()
    expiry = models.DateTimeField()
    issued_date = models.DateTimeField()
    wallet = models.ManyToOneRel()
    account = models.ManyToOneRel()
    issuer = models.CharField()    

class Third_Party(models.model):
    name = models.CharField()
    id = models.CharField()
    type = models.CharField()
    transaction_account = models.IntegerField()
    account = models.ForeignKey()
    currency = models.CharField()

class Notifications(models.model):
    transaction = models.CharField()
    transaction_id = models.BigAutoField()
    transaction_amount = models.BigAutoField()
    Customer_id = models.BigAutoField()
    status = models.CharField()
    transaction_number =models.CharField()
    date_time = models.DateTimeField()
    recipient = models.OneToOneField
    transaction_description = models.CharField()

class Receipt(models.model):
    receipt_type = models.CharField()
    receipt_date = models.DateTimeField()
    bill_number = models.BigAutoField()
    total_amount = models.IntegerField()
    transaction = models.ForeignKey()
    receipt_file = models.FieldFile()

class Loan(models.model):
    loan_id = models.BigIntegerField()
    loan_type = models.CharField()
    amount = models.BigIntegerField()
    datetime = models.DateTimeField()
    Wallet = models.ForeignKey()
    intrest_rate = models.IntegerField()
    payment_due_date = models.DateTimeField()
    loan_balance = models.IntegerField()
    guaranter = models.ForeignKey() 


class Reward(models.model):
    name = models.CharField()
    customer_id = models.BigAutoField()
    gender = models.CharField()
    points = models.IntegerField()
    date_of_reward = models.DateTimeField()
    recipient = models.OneToOneField()