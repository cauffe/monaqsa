from django.contrib import admin

from main.models import Company, Company_documents, Users_info, Tender, Item, Quotation

# Register your models here.

admin.site.register(Company)
admin.site.register(Company_documents)
admin.site.register(Users_info)
admin.site.register(Tender)
admin.site.register(Item)
admin.site.register(Quotation)