from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Company(models.Model):
    user = models.OneToOneField(User)
    comapny_name = models.CharField(max_length=255, null=True)
    street = models.CharField(max_length=60, null=True)
    city = models.CharField(max_length=40, null=True)
    post_code = models.CharField(max_length=40, null=True)
    country = models.CharField(max_length=40, null=True)
    po_box = models.CharField(null=True)
    website = models.CharField(max_length=255, null=True)
    logo = models.ImageField(upload_to="logos")
    tel_number = models.CharField(null=True)
    fax_number = models.CharField(null=True)
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
    legal_structure = models.CharField(max_length=255, choices=legal_structure_type, default='Limited Liability Company', null=True)
    mobile = models.CharField(null=True)

    def __unicode__(self):
        return self.name


class Tender(models.Model):
    name = models.CharField(max_length=255)
    opening_date = models.DateField()
    closing_date = models.DateField()
    company = models.ForeignKey('main.Company')

    def __unicode__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null=True)
    quantity = models.FloatField()
    tender = models.ForeignKey('main.Tender')

    def __unicode__(self):
        return self.name


class Quotation(models.Model):
    unit_price = models.FloatField()
    total_price = models.FloatField()
    note = models.CharField(max_length=255, null=True)
    company = models.ForeignKey('main.Company')
    item = models.ManyToManyField('main.Item')
    tender = models.ForeignKey('main.Tender')

    def __unicode__(self):
        return self.company.name
