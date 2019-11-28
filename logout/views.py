from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.http import Http404
from login.models import visitor,currently_login
from django.utils import timezone
from . import send_mail
from . import forms
from . import sms
import _thread

def index(request):
	form = forms.logout()
	if request.method=='POST':
		form = forms.logout(request.POST,request.FILES)
		if form.is_valid():
			phonenumber = form.cleaned_data['phonenumber']
			li = visitor.objects.all().filter(phone_num = phonenumber)
			for i in li:
				if i.status == True:
					obj = i
					obj.check_out = timezone.now()
					obj.status = False
					msg = sms.message(obj)
					mailing = send_mail.sending(obj)
					try:
						_thread.start_new_thread(mailing.start,())
						pass
					except:
						print('Error occured while e-mailing at logout(object_id= '+str(obj.pk)+')')
					try:
						_thread.start_new_thread(msg.start,())
						pass
					except:
						print('Error occured while messaging at logout(object_id= '+str(obj.pk)+')')
					obj.save()
					obj_ = currently_login.objects.get(visitor_email = obj.email)
					obj_.delete()
					return redirect('logout:done',obj.pk)
			return render(request,'logout/checkout.html',{'form':form,'error':1})
	return render(request,'logout/checkout.html',{'form':form,'error':0})

def done(request,obj_id):
	if visitor.objects.filter(pk=obj_id).exists():
		pass
	else:
		raise Http404
	if visitor.objects.get(pk=obj_id).status == False:
		return render(request,'logout/done.html',{})
	else:	
		return redirect('login:done',obj_id)
