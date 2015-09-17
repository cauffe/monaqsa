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
	
	context['tenders']= tenders

	Quotations = Quotation.objects.all()
	
	context['quotation_view']= Quotations

	return render_to_response('home.html', context, context_instance=RequestContext(request))


def signup(request):

	context = {}

	form = UserSignUp()
	context['form'] = form

	if request.method == 'POST':
		form = UserSignUp(request.POST)
		if form.is_valid():

			name = form.cleaned_data['name']
			email = form.cleaned_data['email']
			password = form.cleaned_data['password']

			try:
				User.objects.create_user(name, email, password)
				context['valid'] = "Thank You For Sign Up!"

				auth_user = authenticate(username=name, password=password)
				login(request, auth_user)
				return HttpResponseRedirect('/home/')


			except IntegrityError, e:
				context['valid'] = "A User With That Name Already Exsist"

		else:
			context['valid'] = form.errors

	if request.method == 'GET':
		context['valid'] = "Please Sign Up!"


	return render_to_response('signup.html', context, context_instance=RequestContext(request))
	

def login_view(request):
	
	context = {}

	context['form'] = UserLogin()

	username = request.POST.get('username', None)
	password = request.POST.get('password', None)

	auth_user = authenticate(username=username, password=password) #returns None, why?

	if auth_user is not None:
		if auth_user.is_active:
			login(request, auth_user)
			context['valid'] = "Login Successful"

			return HttpResponseRedirect('/home/')
		else:
			context['valid'] = "Invalid User"
			return render_to_response('login.html', context, context_instance=RequestContext(request))

	else:
		context['valid'] = "please enter a User Name"
		return render_to_response('login.html', context, context_instance=RequestContext(request))


	return render_to_response('login.html', context, context_instance=RequestContext(request))

def logout_view(request):

	logout(request)

	return HttpResponseRedirect('/home/')