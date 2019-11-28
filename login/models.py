from django.db import models
from django.utils import timezone

class visitor(models.Model):
	firstname = models.CharField(max_length=250)
	lastname = models.CharField(max_length=250)
	email = models.CharField(max_length=250)
	phone_num = models.CharField(max_length=250)
	check_in = models.DateTimeField(default = timezone.now(), blank=True)
	check_out = models.DateTimeField(blank=True , default = timezone.now())
	status = models.BooleanField(default=True)

	def __str__(self):
		return self.firstname+" "+self.lastname+" "+str(self.pk);

class host(models.Model):
	visitor = models.ForeignKey(visitor,on_delete=models.CASCADE)
	firstname = models.CharField(max_length=250)
	lastname = models.CharField(max_length=250)
	email = models.CharField(max_length=250)
	phone_num = models.CharField(max_length=250)

	def __str__(self):
		return self.firstname+" "+self.lastname;

class currently_login(models.Model):
	visitor_firstname = models.CharField(max_length=250)
	visitor_lastname = models.CharField(max_length=250)
	visitor_email = models.CharField(max_length=250)
	visitor_phone_num = models.CharField(max_length=250)
	host_firstname = models.CharField(max_length=250)
	host_lastname = models.CharField(max_length=250)
	host_email = models.CharField(max_length=250)
	host_phone_num = models.CharField(max_length=250)
