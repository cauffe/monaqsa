from django.shortcuts import render
from main.models import Company, Tender, Quotation
from django.http import HttpResponse, HttpResponseRedirect
from main.forms import UserSignUp, UserLogin, CreateTender, CreateTender, CreateItem, EditTender, EditQuote, EditItem


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


def quotation_list(request):
    context = {}
    quotation = Quotation.objects.all()
    context['quotations'] = quotations

    return render(request, 'quotations.html', context)


def quotation_detail(request, pk):
    context = {}
    quotation = Quotation.objects.get(pk=pk)
    context['quotation'] = quotation

    return render(request, 'qoutation.html', context)


def tender_create(request):
    context = {}
    form = CreateTender()
    context['from'] = form
    if requested.method == "POST":
        form = CreateTender(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            context['valid'] = "Tender Created"
    else:
        context['errors'] = form.errors
    return render(request, 'tender_create.html', context)


def quote_create(request):
    context = {}
    form = CreateQuote()
    context['form'] = form
    if requested.method == "POST":
        form = CreateQuote(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            context['valid'] = "Quote Created"
    else:
        context['errors'] = form.errors
    return render(request, 'quote_create.html', context)