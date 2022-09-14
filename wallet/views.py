from inspect import trace
from django.shortcuts import render
from wallet.models import Account, Card, Currency, Customer, Loan, Notification, Receipt, Reward, ThirdParty, Transaction, Wallet
from .forms import CustomerRegistrationForm, RewardRegistrationForm, WalletRegistrationForm,CardRegistrationForm,ThirdpartyRegistrationForm,ReceiptRegistrationForm
from .forms import CurrencyRegistrationForm, AccountRegistrationForm,TransactionRegistrationForm,NotificationRegistrationForm
from .forms import LoanRegistrationForm
# The puporse of this view.py is to handle https
# A http request is composed by a request and a response fromthe cloud.
# This  is where the customer enters and saves data .
# Accepts only one argument(request)
# Create your views here.
# Then get our route via url.py

def register_customer(request):
    if request.method == 'POST':
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
          form.save()

    else:
        form=CustomerRegistrationForm()
    return render (request,"wallet/register_customer.html",{"form":form})
def list_Customers(request):
    people= Customer.objects.all()
    return render (request,"wallet/list_Customers.html",{"people":people})


def register_currency(request):
    if request.method == 'POST':
        form = CurrencyRegistrationForm(request.POST)
        if form.is_valid():
          form.save()

    else:
       form = CurrencyRegistrationForm()
    return render (request,"wallet/register_currency.html",{"form" : form})

def list_currency(request):
    bills= Currency.objects.all()
    return render (request,"wallet/list_currency.html",{"bills":bills})


def register_wallet(request):
     if request.method == 'POST':
        form =WalletRegistrationForm(request.POST)
        if form.is_valid():
          form.save()

     else:
       form = WalletRegistrationForm()

     return render (request,"wallet/register_wallet.html", {"form":form})
def list_wallet(request):
    wallets= Wallet.objects.all()
    return render (request,"wallet/list_wallets.html",{"wallets":wallets})


def register_account(request):
      if request.method == 'POST':
        form =AccountRegistrationForm(request.POST)
      if form.is_valid():
          form.save()

      else:
        form = AccountRegistrationForm()
      return render (request, "wallet/register_account.html", {"form":form})

def list_account(request):
    accounts= Account.objects.all()
    return render (request,"wallet/list_account.html",{"accounts":accounts})


def register_transaction(request):
     if request.method == 'POST':
        form =TransactionRegistrationForm(request.POST)
     if form.is_valid():
          form.save()

     else:
       form = TransactionRegistrationForm()
     return render (request, "wallet/register_transaction.html", {"form":form})

def list_transaction(request):
    transactions= Transaction.objects.all()
    return render (request,"wallet/list_transaction.html",{"transactions":transactions})


def register_card(request):
    if request.method == 'POST':
        form =CardRegistrationForm(request.POST)
    if form.is_valid():
          form.save()

    else:
       form = CardRegistrationForm()
    return render (request, "wallet/register_card.html", {"form":form})

def list_card(request):
    cards= Card.objects.all()
    return render (request,"wallet/list_card.html",{"cards":cards})


def register_thirdparty(request):
    if request.method == 'POST':
        form =ThirdpartyRegistrationForm(request.POST)
    if form.is_valid():
          form.save()

    else:
         form = ThirdpartyRegistrationForm()
    return render (request,"wallet/register_thirdparty.html", {"form":form})

def list_thirdparty(request):
    thirdparty= ThirdParty.objects.all()
    return render (request,"wallet/list_thirdparty.html",{"thirdparty":thirdparty})


def register_notification(request):
    if request.method == 'POST':
        form =NotificationRegistrationForm(request.POST)
    if form.is_valid():
          form.save()

    else:
       form = NotificationRegistrationForm()
    return render (request, "wallet/register_notification.html", {"form":form})

def list_notifications(request):
    notify= Notification.objects.all()
    return render (request,"wallet/list_notification.html",{"notify":notify})


def register_receipt(request):
    if request.method == 'POST':
        form =ReceiptRegistrationForm(request.POST)
    if form.is_valid():
          form.save()

    else:
        form = ReceiptRegistrationForm()

    return render (request, "wallet/register_receipt.html", {"form":form})

def list_receipt(request):
    receipts= Receipt.objects.all()
    return render (request,"wallet/list_receipt.html",{"receipts":receipts})


def register_loan(request):
    if request.method == 'POST':
        form =LoanRegistrationForm(request.POST)
    if form.is_valid():
          form.save()

    else:
        form = LoanRegistrationForm()

    return render(request, "wallet/register_loan.html",{"form":form})

def list_loan(request):
    loans= Loan.objects.all()
    return render (request,"wallet/list_loan.html",{"loans":loans})



def register_reward(request):
    if request.method == 'POST':
        form =RewardRegistrationForm(request.POST)
    if form.is_valid():
          form.save()

    else:
     form = RewardRegistrationForm()

    return render (request, "wallet/register_reward.html", {"form":form})

def list_rewards(request):
    rewards= Reward.objects.all()
    return render (request,"wallet/list_reward.html",{"rewards":rewards})



# geting Querys by rendering the list of all customers
# def list_customers(request):
#     Customer = Customer.object.all()

#     return render(request,"wallet/customer_list.html,
#     {"customers:customers"}")