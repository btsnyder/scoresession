from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^session/$', views.SessionView, name='session'),
    url(r'^loading/$', views.LoadingView, name='loading'),
]
