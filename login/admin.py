from django.contrib import admin
from .models import visitor,host,currently_login

# Register your models here.
admin.site.register(visitor)
admin.site.register(host)
admin.site.register(currently_login)
