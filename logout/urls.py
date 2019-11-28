from django.conf.urls import url
from . import views
app_name = 'logout'
urlpatterns = [
    url(r'^(?P<obj_id>[0-9]+)/done',views.done,name='done'),
    url(r'^', views.index,name='index'),
]
