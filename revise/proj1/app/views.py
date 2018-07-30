# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.decorators.csrf import csrf_exempt

from django.shortcuts import render
from django.shortcuts import redirect
from django.db.models import Q
from models import *

# Create your views here.
@csrf_exempt
def register(request):
	if request.method=="GET":
		return render(request,"reg.html",{})
	elif request.method=="POST":
		context={}
		name=request.POST['name']
		password=request.POST['password']
		contact=request.POST['contact']
		user_type=request.POST['user_type']
		if User.objects.filter(username=name,password=password).exists():
			context['message']='Username already exists'
			return render (request,"reg.html",context)
			
		else:
			aaa=User(username=name, password=password, contact=contact, 		user_type=user_type)
			aaa.save()

		#context['name']=name
		#context['password']=password
		#context['contact']=contact

		return redirect ('/login')
	

@csrf_exempt
def login(request):
	if 'name' in request.session:
		if request.session['user_type']=='librarian':
			return redirect('/librarian_dashboard')
		elif request.session['user_type']=='student':
			return redirect('/student_dashboard')
	
	if request.method=="GET":
		return render(request,"login.html",{})
	elif request.method=="POST":
		context={}
		name=request.POST['name']
		password=request.POST['password']
	
		if User.objects.filter(username=name).exists():
			if User.objects.filter(username=name,password=password).exists():
				user_obj=User.objects.get(username=name)
				request.session['name']=user_obj.username
				request.session['user_type']=user_obj.user_type
				if user_obj.user_type=='librarian':
					return redirect('/librarian_dashboard')
				#message=user_obj.username
				#message+=' '+user_obj.contact
				if user_obj.user_type=='student':
					return redirect('/student_dashboard')
			else:
				context['message']='Username & password do not match'
		else:
			context['message']='Username does not exist'
		return render(request,"login.html",context)

@csrf_exempt
def start(request):
	if 'name' in request.session:
		obj=User.objects.get(username=request.session['name'])
		if obj.user_type=='student':
			return redirect('/student_dashboard')
		else:
			return redirect('/librarian_dashboard') 
	else:
		return redirect('/login')


@csrf_exempt
def logout(request):
	if 'name' in request.session:
		del request.session['name']
		del request.session['user_type']
	return redirect('/login')

def student(request):
	if 'name' in request.session:
		context={}
		obj=Books.objects.all()
		context['books']=obj
		return render(request,'student_dashboard.html',context)
	else:
		return redirect('/login')

def librarian(request):
	if 'name' in request.session:
		context={}
		obj=Books.objects.all()
		context['books']=obj
		return render(request,'librarian_dashboard.html',{})
	else:
		return redirect('/login')

def book_details(request):
	context={}
	id1=request.GET["book_id"]			#storing the id in a variable id1
	request.session["book_id"]=id1
	obj=Books.objects.get(id=id1)   #create an object to access the object corres to the id
	#summary=obj.summary				#object use karke table se summary
	context = {'Name':obj.book_name, 'Author':obj.author_name, 'copies':obj.copies, 'Rating':obj.rating, 'Summary':obj.summary }
	return render(request,'book_details.html',context)

def view_profile(request):
	if 'name' in request.session:
		context={}
		name=request.session['name']
		obj=User.objects.get(username=name)
		context={'username':obj.username, 'password':obj.password, 'contact':obj.contact, 'user_type':obj.user_type}
		return render(request,'profile.html',context)

@csrf_exempt
def search(request):
	context={}
	auth_title=request.POST['author']
	book_title=request.POST['title']
	obj=Books.objects.filter(Q(author_name=auth_title) | Q(book_name=book_title) )
	context['booklist']=obj
	return render(request,'book_list.html',context)

@csrf_exempt
def requestbook(request):
	id1=request.session["book_id"]
	obj=Books.objects.get(id=id1)
	name=request.session['name']
	obj=User.objects.get(username=name)
	context=context = {'Name':obj.book_name, 'Author':obj.author_name, 'copies':obj.copies, 'Rating':obj.rating, 'Summary':obj.summary }
	if BookIssue.objects.filter(Q(StudentName__username=request.session['username']) & Q(Q(BookStatus='booked') | Q(BookStatus='pickedup'))).exists():
		context['message']='Issue suspended,Return previous issued books first to issue a new book'
		return render(request,'bok_details.html',context)
	
	
	

		

#@csrf_exempt
#def data(request):
#	context={}
#	name=request.POST['name']
#	password=request.POST['password']
#	contact=request.POST['contact']
#	type=request.POST['type']
#	if User.objects.filter(username=name,password=password).exists():
#		print 'Username exists'
#	else:
#		aaa=User(username=name, password=password, contact=contact, type=type)
#		aaa.save()

#	context['name']=name
#	context['password']=password
#	context['contact']=contact

#	return render(request,"data.html",context)

#LOGIN
#take input
#check if username exists
#check if password matches
#see usertype and redirect accordingly
#@csrf_exempt
#def check_function(request):
#	context={}
#	name=request.POST['name']
#	password=request.POST['password']
	
#	if User.objects.filter(username=name).exists():
#		if User.objects.filter(username=name,password=password).exists():
#			user_obj=User.objects.get(username=name)
#			message=user_obj.username
#			message+=' '+user_obj.contact
#		else:
#			message='Username & password do not match'
#	else:
#		message='Username does not exist'
#	context['message']=message
#	return render(request,"login_page.html",context)


