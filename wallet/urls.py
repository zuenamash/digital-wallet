from django.urls import path
from .views import list_account, list_card, list_currency, list_Customers, list_loan, list_notifications, list_receipt, list_rewards,list_thirdparty, list_transaction, list_wallet, register_card, register_customer, register_notification, register_receipt, register_thirdparty, register_transaction
from .views import register_currency
from .views import register_wallet
from .views import register_account,register_loan,register_reward
from .import views


urlpatterns =[ 
path("register/",register_customer,name="registrationRegister"),
path("registercurrency/",register_currency, name="registrationCurrency"),
path("registerwallet/", register_wallet, name="registrationWallet"),
path("registeraccount/", register_account, name = "registrationAccount"),
path ("registertransaction/", register_transaction, name = "registrationTransaction"),
path ("registercard/", register_card,name="registrationCard"),
path ("registerthirdparty/", register_thirdparty, name="registrationThirdparty"),
path ("registernotification/", register_notification, name="registrationNotification"),
path ("registerreceipt/", register_receipt, name="registrationReceipt"),
path ("registerloan/", register_loan, name="registrationLoan"),
path ("registerreward/", register_reward, name="registrationReward"),
path ("customers/",list_Customers,name="customers_list"),
path ("currency/",list_currency,name="currency_list"),
path ("wallet/",list_wallet,name="wallet_list"),
path ("account/",list_account,name="account_list"),
path ("transaction/",list_transaction,name="transaction_list"),
path ("card/",list_card,name="card_list"),
path ("thirdparty/",list_thirdparty,name="thirdpary_list"),
path ("notification/",list_notifications,name="notification_list"),
path ("receipt/",list_receipt,name="receipt_list"),
path ("loan/",list_loan,name="loan_list"),
path ("reward/",list_rewards,name="reward_list"),
]