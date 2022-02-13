from django.conf.urls import url
from basic import views
app_name='zico'

urlpatterns=[
     url(r'^relative/',views.relative,name='relative'),
     url(r'^other/',views.other,name='other'),
     url(r'^$',views.home,name='home'),
]
