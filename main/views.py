from django.shortcuts import render, render_to_response
from main.models import Company, Tender, Quotation
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from main.forms import UserSignUp, UserLogin, CreateTender, CreateTender, CreateItem, EditTender, EditQuote, EditItem
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext

# Create your views here.

def signup(request):
    context = {}

    form = UserSignUp()

    context['form'] = form

    if request.method == 'POST':
        form = UserSignUp(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            email = None

            new_user = User.objects.create_user(username, email, password)

            auth_user = authenticate(username=username, password=password)


            login(request, auth_user)

            return HttpResponseRedirect('/list_view/')

    return render_to_response('signup.html', context, context_instance=RequestContext(request))


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
    if request.method == "POST":
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
    if request.method == "POST":
        form = CreateQuote(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            context['valid'] = "Quote Created"
    else:
        context['errors'] = form.errors
    return render(request, 'quote_create.html', context)