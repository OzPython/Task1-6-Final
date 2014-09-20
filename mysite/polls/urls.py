from django.conf.urls import patterns, url

from polls import views

urlpatterns = patterns('',
    
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^specifics/(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^specifics/(?P<pk>\d+)/results/$', views.ResultView.as_view(), name='results'),
    url(r'^specifics/(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
)
