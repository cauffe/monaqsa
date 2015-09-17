# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=60)),
                ('city', models.CharField(max_length=40)),
                ('county', models.CharField(max_length=40)),
                ('country', models.CharField(max_length=40)),
                ('po_box', models.IntegerField(null=True)),
                ('website', models.CharField(max_length=255, null=True)),
                ('email', models.CharField(max_length=255)),
                ('tel_number', models.IntegerField()),
                ('fax_number', models.IntegerField(null=True)),
                ('legal_structure', models.CharField(default=b'Limited Liability Company', max_length=255, choices=[(b'SOLO TRADER', b'Solo Trader'), (b'LIMITED LIABILITY COMPANY', b'Limited Liability Company'), (b'PARTNERSHIP', b'Partnership'), (b'PUBLIC COMPANY', b'Public Company'), (b'FREE ZONE ENTERPRISE', b'Free Enterprise'), (b'GOVERMENT BODY', b'Goverment Body'), (b'OTHER', b'Other'), (b'LEGAL STRUCTURE NOT LISTED', b'Legal Structure Not Listed')])),
                ('buyer_company_type', models.BooleanField()),
                ('supplier_company_type', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Company_documents',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('license', models.ImageField(null=True, upload_to=b'company')),
                ('authentication_of_signature', models.ImageField(null=True, upload_to=b'company')),
                ('official_letter', models.ImageField(null=True, upload_to=b'company')),
                ('company', models.OneToOneField(to='main.Company')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255, null=True)),
                ('quantity', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Quotation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('unit_price', models.FloatField()),
                ('total_price', models.FloatField()),
                ('note', models.CharField(max_length=255, null=True)),
                ('company', models.ForeignKey(to='main.Company')),
                ('item', models.ManyToManyField(to='main.Item')),
            ],
        ),
        migrations.CreateModel(
            name='Tender',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subject', models.CharField(max_length=255)),
                ('opening_date', models.DateField()),
                ('closing_date', models.DateField()),
                ('tender_type', models.CharField(default=b'Public', max_length=255, choices=[(b'PUBLICE', b'Public'), (b'PRIVATE', b'private')])),
                ('company', models.ForeignKey(to='main.Company')),
            ],
        ),
        migrations.CreateModel(
            name='Users_info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=255)),
                ('Last_name', models.CharField(max_length=255)),
                ('job_title', models.CharField(max_length=255)),
                ('mobile', models.IntegerField()),
                ('email', models.CharField(max_length=255)),
                ('company', models.ForeignKey(to='main.Company')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='tender',
            field=models.ForeignKey(to='main.Tender'),
        ),
    ]
