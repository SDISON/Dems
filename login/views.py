from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import visitor,host,currently_login
from django.http import Http404
from . import forms
from . import send_mail
from . import sms
import _thread

def remove(request,obj):
	obj_ = visitor.objects.get(pk = obj)
	obj_.delete()
	obj__ = currently_login.objects.get(email = obj_.email)
	obj__.delete()
	return redirect('login:index')

def index(request):
	form = forms.checkin_vis()
	if request.method=='POST':
		form = forms.checkin_vis(request.POST,request.FILES)
		if form.is_valid():
			firstname = form.cleaned_data['firstname']
			lastname = form.cleaned_data['lastname']
			email = form.cleaned_data['email']
			phonenumber = form.cleaned_data['phonenumber']
			obj = visitor()	
			obj.firstname = firstname
			obj.lastname = lastname
			obj.email = email
			obj.phone_num = phonenumber
			li = visitor.objects.all().filter(email = email)
			for i in li:
				if i.status == True:
					return render(request,'login/index.html',{'form':form,'error':1})
			li = visitor.objects.all().filter(phone_num = phonenumber)
			for i in li:
				if i.status == True:
					return render(request,'login/index.html',{'form':form,'error':1})
			else:
				obj.save()
			return redirect('login:save',obj.pk)
	return render(request,'login/index.html',{'form':form,'error':0})

def save(request,obj_id):
	form = forms.checkin_host()
	if visitor.objects.filter(pk=obj_id).exists():
		pass
	else:
		raise Http404
	if host.objects.filter(visitor = visitor.objects.get(pk = obj_id)).exists():
		raise Http404
	if request.method=='POST':
		form = forms.checkin_host(request.POST)
		if form.is_valid():
			firstname = form.cleaned_data['firstname']
			lastname = form.cleaned_data['lastname']
			email = form.cleaned_data['email']
			phonenumber = form.cleaned_data['phonenumber']
			obj = host()
			obj.visitor = visitor.objects.get(pk=obj_id)
			obj.firstname = firstname
			obj.lastname = lastname
			obj.email = email
			obj.phone_num = phonenumber
			if obj.email == obj.visitor.email:
				return render(request,'login/save.html',{'pk':obj_id,'form':form,'error':1})
			elif obj.phone_num == obj.visitor.phone_num:
				return render(request,'login/save.html',{'pk':obj_id,'form':form,'error':2})
			elif host.objects.filter(visitor = obj.visitor).exists():
				return render(request,'login/save.html',{'pk':obj_id,'form':form,'error':3})
			else:
				mailing = send_mail.sending(obj)
				msg = sms.message(obj)
				try:
					_thread.start_new_thread(mailing.start,())
					pass
				except:
					print('Error occured while e-mailing at login(object_id= '+str(obj_id)+')')
				try:
					_thread.start_new_thread(msg.start,())
					pass
				except:
					print('Error occured while messaging at logout(object_id= '+str(obj_id)+')')
				obj.save()
				temp = currently_login()
				temp.visitor_firstname = obj.visitor.firstname
				temp.visitor_lastname = obj.visitor.lastname
				temp.visitor_email = obj.visitor.email
				temp.visitor_phone_num = obj.visitor.phone_num
				temp.host_firstname = obj.firstname
				temp.host_lastname = obj.lastname
				temp.host_email = obj.email
				temp.host_phone_num = obj.phone_num
				temp.save()
				return redirect('login:done',obj_id)
	return render(request,'login/save.html',{'pk':obj_id,'form':form,'error':0})

def done(request,obj_id):
	if visitor.objects.filter(pk=obj_id).exists():
		pass
	else:
		raise Http404
	if visitor.objects.get(pk=obj_id).status == False:
		return redirect('logout:done',obj_id)
	else:
		return render(request,'login/done.html',{})

