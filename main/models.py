from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Company(models.Model):
    user = models.OneToOneField(User)
    comapny_name = models.CharField(max_length=254, null=True)
    street = models.CharField(max_length=60, null=True)
    city = models.CharField(max_length=40, null=True)
    post_code = models.CharField(max_length=40, null=True)
    country = models.CharField(max_length=254, null=True)
    po_box = models.CharField(max_length=254, null=True)
    website = models.CharField(max_length=254, null=True)
    logo = models.ImageField(upload_to="logos")
    tel_number = models.CharField(max_length=254, null=True)
    fax_number = models.CharField(max_length=254, null=True)
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
    legal_structure = models.CharField(max_length=254, choices=legal_structure_type, default='Limited Liability Company', null=True)
    mobile = models.CharField(null=True, max_length=254)

    def __unicode__(self):
        return self.name


class Tender(models.Model):
    company = models.ForeignKey('main.Company')
    name = models.CharField(max_length=254)
    opening_date = models.DateField()
    closing_date = models.DateField()
   
    def __unicode__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=254)
    description = models.CharField(max_length=254, null=True)
    quantity = models.FloatField()
    tender = models.ForeignKey('main.Tender')
    image = models.ImageField(upload_to='items')

    def __unicode__(self):
        return self.name


class Quotation(models.Model):
    unit_price = models.FloatField()
    quantity = models.CharField(max_length=254)
    total_price = models.FloatField()
    comment = models.CharField(max_length=254, null=True)
    company = models.ForeignKey('main.Company')
    item = models.ManyToManyField('main.Item')
    tender = models.ForeignKey('main.Tender')

    def __unicode__(self):
        return self.company.name
