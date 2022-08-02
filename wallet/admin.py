
from django.contrib import admin
from .models import Customer,Account,Transaction,Notification,Receipt,Reward
from.models import Currency
from .models import Wallet
from.models import ThirdParty
from .models import Card
from .models import Loan


admin.site.register(Customer)
admin.site.register(Currency)
admin.site.register(Wallet)
admin.site.register(Account)
admin.site.register(Transaction)
admin.site.register(Card)
admin.site.register(ThirdParty)
admin.site.register(Notification)
admin.site.register(Receipt)
admin.site.register(Loan)
admin.site.register(Reward)



# Register your models here.
