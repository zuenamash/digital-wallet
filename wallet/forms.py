# from concurrent.futures.thread import _worker
# from dataclasses import fields
# from curses.ascii import TAB
# from dataclasses import fields
# from pyexpat import model
# from dataclasses import field, fields
# from pyexpat import model
from django import forms
from .models import Account, Card, Currency, Customer, Loan, Notification, Receipt, Reward, ThirdParty, Transaction, Wallet


class CustomerRegistrationForm(forms.ModelForm):
    class Meta:
         model= Customer
         fields = "__all__"
widgets={
             "first_name":forms.TextInput(attrs={ 'class': "form-control"}),
             "last_name": forms.TextInput(attrs={ 'class': "form-control"}),
             "address": forms.TextInput(attrs={ 'class': "form-control"}),
             "email": forms.TextInput(attrs={ 'class': "form-control"}),
             "phone_number": forms.TextInput(attrs={ 'class': "form-control"}),
             "gender": forms.Select(attrs={ 'class': "form-control"}),
             "nationality": forms.TextInput(attrs={ 'class': "form-control"}),
             "age": forms.TextInput(attrs={ 'class': "form-control"}),
             "profile_picture":forms.ClearableFileInput(attrs={ 'class': "form-control"}),
}
   

    # How to create form in django to collect data for the entities.
    # A mete class provides data of the clss your are inheriting from
class CurrencyRegistrationForm(forms.ModelForm):
    class Meta:
         model= Currency
         fields = "__all__"
widgets={
          "country":forms.TextInput(attrs={ 'class': "form-control"}),
          "symbol":forms.TextInput(attrs={ 'class': "form-control"}),
          "amount":forms.TextInput(attrs={ 'class': "form-control"}),

}

class WalletRegistrationForm(forms.ModelForm):
     class Meta:
          model= Wallet
          fields = "__all__"

widgets={
      "balance":forms.TextInput(attrs={ 'class': "form-control"}),
      "customer":forms.TextInput(attrs={ 'class': "form-control"}),
      "amount":forms.TextInput(attrs={ 'class': "form-control"}),
      "date_created":forms.TextInput(attrs={ 'class': "form-control"}),
      "status":forms.TextInput(attrs={ 'class': "form-control"}),
      "currency":forms.TextInput(attrs={ 'class': "form-control"}),
      "history":forms.TextInput(attrs={ 'class': "form-control"}),
      "pin":forms.TextInput(attrs={ 'class': "form-control"}),

}

class AccountRegistrationForm(forms.ModelForm):
     class Meta:
          model= Account
          fields = "__all__"
widgets={
     "account_name":forms.TextInput(attrs={'class':"form-control"}),
     "account_number":forms.TextInput(attrs={'class':"form-control"}),
     "account_type":forms.TextInput(attrs={'class':"form-control"}),
     "account_balance":forms.TextInput(attrs={'class':"form-control"}),
     "account_name":forms.TextInput(attrs={'class':"form-control"}),
     "wallet":forms.TextInput(attrs={'class':"form-control"}),

}

class TransactionRegistrationForm(forms.ModelForm):
     class Meta:
          model = Transaction
          fields = "__all__"
widgets={
     "message ":forms.TextInput(attrs={'class':"form-control"}),
     "wallet":forms.TextInput(attrs={'class':"form-control"}),
     "transaction_description":forms.TextInput(attrs={'class':"form-control"}),
     "transaction_amount":forms.TextInput(attrs={'class':"form-control"}),
     "transaction_type":forms.TextInput(attrs={'class':"form-control"}),
     "origin_account ":forms.TextInput(attrs={'class':"form-control"}),
     "destination_account":forms.TextInput(attrs={'class':"form-control"}),


}

class CardRegistrationForm(forms.ModelForm):
     class Meta:
          model=Card
          fields = "__all__"
widgets={
     "card_number":forms.TextInput(attrs={'class':"form-control"}),
     "card_type":forms.TextInput(attrs={'class':"form-control"}),
     "expiry_date":forms.TextInput(attrs={'class':"form-control"}),
     "security_code":forms.TextInput(attrs={'class':"form-control"}),
     "date_of_issue":forms.TextInput(attrs={'class':"form-control"}),
     "wallet":forms.TextInput(attrs={'class':"form-control"}),
     "account":forms.TextInput(attrs={'class':"form-control"}),
     "issuer":forms.TextInput(attrs={'class':"form-control"}),

}


class ThirdpartyRegistrationForm(forms.ModelForm):
     class Meta:
          model = ThirdParty
          fields = "__all__"
widgets={
      "account":forms.TextInput(attrs={ 'class': "form-control"}),
      "transaction_amount":forms.TextInput(attrs={ 'class': "form-control"}),
      "currency":forms.TextInput(attrs={ 'class': "form-control"}),
      "date_of_issue":forms.TextInput(attrs={ 'class': "form-control"}),
      "wallet":forms.TextInput(attrs={ 'class': "form-control"}),
      "isuer":forms.TextInput(attrs={ 'class': "form-control"}),

}
class NotificationRegistrationForm(forms.ModelForm):
     class Meta:
          model = Notification
          fields= "__all__"

widgets={
       "message":forms.TextInput(attrs={ 'class': "form-control"}),
       "date":forms.TextInput(attrs={ 'class': "form-control"}),
       "recipient":forms.TextInput(attrs={ 'class': "form-control"}),
       "title":forms.TextInput(attrs={ 'class': "form-control"}),

}

class ReceiptRegistrationForm(forms.ModelForm):
     class Meta:
          model = Receipt
          fields = "__all__"
widgets={
      "recipient_type":forms.TextInput(attrs={ 'class': "form-control"}),
      "date":forms.TextInput(attrs={ 'class': "form-control"}),
      "recipient_number":forms.TextInput(attrs={ 'class': "form-control"}),
      "amount":forms.TextInput(attrs={ 'class': "form-control"}),
      "transaction":forms.TextInput(attrs={ 'class': "form-control"}),
      "recipient_file":forms.TextInput(attrs={ 'class': "form-control"}),

}

class LoanRegistrationForm(forms.ModelForm):
     class Meta:
          model= Loan
          fields = "__all__"
widgets={
     "loan_id":forms.TextInput(attrs={ 'class': "form-control"}),
     "loan_type":forms.TextInput(attrs={ 'class': "form-control"}),
     "loan_balance":forms.TextInput(attrs={ 'class': "form-control"}),
     "amount":forms.TextInput(attrs={ 'class': "form-control"}),
     "guaranter":forms.TextInput(attrs={ 'class': "form-control"}),
     "issuer":forms.TextInput(attrs={ 'class': "form-control"}),
     "wallet":forms.TextInput(attrs={ 'class': "form-control"}),
}

class RewardRegistrationForm(forms.ModelForm):
     class Meta:
          model= Reward
          fields= "__all__"
widgets={
   "transaction":forms.TextInput(attrs={ 'class': "form-control"}),
   " recipient":forms.TextInput(attrs={ 'class': "form-control"}),
   "date_of_reward":forms.TextInput(attrs={ 'class': "form-control"}),
   "points":forms.TextInput(attrs={ 'class': "form-control"}),

}