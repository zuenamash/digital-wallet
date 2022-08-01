
from django.contrib import admin
from .models import Account, Customer, Notifications, Receipt, Reward, Third_Party, Transaction
from .models import Wallet
from .models import Account
from .models import Card
from .models import Loan


admin.site.register(Customer)
admin.site.register(Wallet)
admin.site.register(Account)
admin.site.register(Transaction)
admin.site.register(Card)
admin.site.register(Third_Party)
admin.site.register(Notifications)
admin.site.register(Receipt)
admin.site.register(Loan)
admin.site.register(Reward)



# Register your models here.
