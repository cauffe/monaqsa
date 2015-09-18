from django.shortcuts import render, render_to_response
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext


from main.models import Company, Company_documents, Users_info, Tender, Item, Quotation
from django.contrib.auth.models import User
from main.forms import UserSignUp, UserLogin


# Create your views here.


def home(request):
    context = {}
    tenders = Tender.objects.all()
    context['tenders'] = tenders
    Quotations = Quotation.objects.all()
    context['quotation_view'] = Quotations
    return render_to_response('home.html', context,
                              context_instance=RequestContext(request))
    context = {}
    companies = Company.objects.all()
    context['companies'] = companies

    return render(request, 'home.html', context)

def signup(request):

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/home')


    context = {}
def tender_list(request):
    context = {}
    tenders = Tender.objects.all()
    context['tenders'] = tenders

    form = UserSignUp()
    context['form'] = form
    return render(request, 'tenders', context)

    if request.method == 'POST':
        form = UserSignUp(request.POST)
        if form.is_valid():
def tender_detail(request, pk):
    context = {}
    tender = Company.objects.get(pk=pk)
    context['tender'] = tender

            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
    return render(request, 'tenders.html', context)

            try:
                User.objects.create_user(name, email, password)
                context['valid'] = "Thank You For Sign Up!"

                auth_user = authenticate(username=name, password=password)
                login(request, auth_user)
                return HttpResponseRedirect('/home/')
def Quotation_list(request):
    context = {}
    quotation = Quotation.objects.all()
    context['quotations'] = quotations

    return render(request, 'quotations.html', context)

            except IntegrityError, e:
                context['valid'] = "A User With That Name Already Exsist"

        else:
            context['valid'] = form.errors
def quotation_detail(request, pk):
    context = {}
    quotation = Quotation.objects.get(pk=pk)
    context['quotation'] = quotation

    if request.method == 'GET':
        context['valid'] = "Please Sign Up!"

    return render_to_response('signup.html', context,
                              context_instance=RequestContext(request))


def login_view(request):

    context = {}

    context['form'] = UserLogin()

    username = request.POST.get('username', None)
    password = request.POST.get('password', None)

    auth_user = authenticate(username=username, password=password)

    if auth_user is not None:
        if auth_user.is_active:
            login(request, auth_user)
            context['valid'] = "Login Successful"

            return HttpResponseRedirect('/home/')
        else:
            context['valid'] = "Invalid User"
            return render_to_response('login.html', context,
                                      context_instance=RequestContext(request))

    else:
        context['valid'] = "please enter a User Name"
        return render_to_response('login.html', context,
                                  context_instance=RequestContext(request))

    return render_to_response('login.html', context,
                              context_instance=RequestContext(request))


def logout_view(request):

    logout(request)

    return HttpResponseRedirect('/home/')    return render(request, 'qoutation.html', context)