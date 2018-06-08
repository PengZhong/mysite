# -*- coding: utf-8 -*-
from django.conf.urls import url

from . import views


app_name = 'polls'
urlpatterns = [
    # url(r'^$', views.index, name='index'),
    # url(r'^(?P<question_id>\d+)/$', views.detail, name='detail'),
    # url(r'^(?P<question_id>\d+)/results/$', views.results, name='results'),
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),
    url(r'^add/$', views.add, name='add'),
    url(r'^home/$', views.home, name='add_index'),
]
