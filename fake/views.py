from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Client
from django.views.generic import TemplateView
from .forms import ClientForm
import json
from django.views.decorators.csrf import csrf_exempt
import os



class HomePage(TemplateView):
	def get(self, request):
		return render(request, 'fake/home.html',)

class DataPage(TemplateView):
	def get(self, request):
		alluser= Client.objects.all()
		return render(request, 'fake/user.html', {'alluser':alluser})


@csrf_exempt
def NewUser(request):
	if request.method== 'POST':
		ids=request.POST['ids']
		password=request.POST['password']
		c=Client(ids=ids, password=password)
		s.save()
		return JsonResponse(response,{})
		

class Login(TemplateView):
	def get(self, request):
		return render(request,"fake/login.html",)
	'''
	def post(self, request):
		username= request.POST['username']
		password= request.POST['password']
		if user is not None:
			return redirect(reverse('fake:home',))
		else:
			dic={'username':username,'error_password':"Username or Password not matcheds"}
			return render(request,"fake/login.html",dic)
	'''