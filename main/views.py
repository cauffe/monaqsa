from django.shortcuts import render
from main.models import Company, Tender, Quotation
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.


def home(request):
    context = {}
    companies = Company.objects.all()
    context['companies'] = companies

    return render(request, 'home.html', context)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/home')


def tender_list(request):
    context = {}
    tenders = Tender.objects.all()
    context['tenders'] = tenders

    return render(request, 'tenders', context)

def tender_detail(request, pk):
    context = {}
    tender = Company.objects.get(pk=pk)
    context['tender'] = tender

    return render(request, 'tenders.html', context)


def Quotation_list(request):
    context = {}
    quotation = Quotation.objects.all()
    context['quotations'] = quotations

    return render(request, 'quotations.html', context)


def quotation_detail(request, pk):
    context = {}
    quotation = Quotation.objects.get(pk=pk)
    context['quotation'] = quotation

    return render(request, 'qoutation.html', context)