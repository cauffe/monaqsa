from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=255, null=False)
    address = models.CharField(max_length=60, null=False)
    city = models.CharField(max_length=40, null=False)
    county = models.CharField(max_length=40, null=False)
    country = models.CharField(max_length=40, null=False)
    po_box = models.IntegerField(null=True)
    website = models.CharField(max_length=255, null=True)
    email = models.CharField(max_length=255, null=False)
    tel_number = models.IntegerField(null=False)
    fax_number = models.IntegerField(null=True)
    legal_structure_type = (
        ('SOLO TRADER', 'Solo Trader'),
        ('LIMITED LIABILITY COMPANY', 'Limited Liability Company'),
        ('PARTNERSHIP', 'Partnership'),
        ('PUBLIC COMPANY', 'Public Company'),
        ('FREE ZONE ENTERPRISE', 'Free Enterprise'),
        ('GOVERMENT BODY', 'Goverment Body'),
        ('OTHER', 'Other'),
        ('LEGAL STRUCTURE NOT LISTED', 'Legal Structure Not Listed')
        )
    legal_structure = models.CharField(max_length=255, choices=legal_structure_type, default='Limited Liability Company')
    buyer_company_type = models.BooleanField()
    supplier_company_type = models.BooleanField()

    def __unicode__(self):
        return self.name


class Company_documents(models.Model):
    license = models.ImageField(upload_to="company", null=True)
    authentication_of_signature = models.ImageField(upload_to="company", null=True)
    official_letter = models.ImageField(upload_to="company", null=True)
    company = models.OneToOneField('main.Company')

    def __unicode__(self):
        return self.license.name


class Users_info(models.Model):
    user = models.OneToOneField(User)
    first_name = models.CharField(max_length=255, null=False)
    Last_name = models.CharField(max_length=255, null=False)
    job_title = models.CharField(max_length=255, null=False)
    mobile = models.IntegerField(null=False)
    email = models.CharField(max_length=255, null=False)
    company = models.ForeignKey('main.Company')

    def __unicode__(self):
        return self.first_name.name
    

class Tender(models.Model):
    name = models.CharField(max_length=255, null=False)
    opening_date = models.DateField()
    closing_date = models.DateField()
    tender_type_types = (
        ('PUBLICE', 'Public'),
        ('PRIVATE', 'private')
        )
    tender_type = models.CharField(max_length=255, choices=tender_type_types, default='Public')
    company = models.ForeignKey('main.Company')

    def __unicode__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=255, null=False)
    description = models.CharField(max_length=255, null=True)
    quantity = models.FloatField(null=False)
    tender = models.ForeignKey('main.Tender')

    def __unicode__(self):
        return self.name


class Quotation(models.Model):
    unit_price = models.FloatField(null=False)
    total_price = models.FloatField(null=False)
    note = models.CharField(max_length=255, null=True)
    company = models.ForeignKey('main.Company')
    item = models.ManyToManyField('main.Item')

    def __unicode__(self):
        return self.company.name
