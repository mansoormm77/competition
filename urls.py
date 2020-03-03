from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from example import views
#connecting views with templates
urlpatterns = [
    url(r'^homepage/$',views.HomePageView.as_view(),name='home'),
    url(r'^$',views.HomePageView.as_view(),name='home'),
    url(r'^about/$',views.AboutPageView.as_view(),name='about'),
    url(r'^visualize/', views.filt, name='my_func'),
]
