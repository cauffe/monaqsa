from django.contrib import admin

from main.models import Company, Tender, Item, Quotation

# Register your models here.

admin.site.register(Company)
admin.site.register(Tender)
admin.site.register(Item)
admin.site.register(Quotation)