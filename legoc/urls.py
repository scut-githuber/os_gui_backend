from django.conf.urls import url

from . import views

urlpatterns = [
    # example:
    # url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^register/$', views.register, name='register'),
    url(r'^node_child/(?P<node_id>[0-2]+)/$', views.node_child, name='node_child'),
    url(r'^node_brother/(?P<node_id>[0-2]+)/$', views.node_brother, name='node_brother'),
    url(r'^node_parent/(?P<node_id>[0-2]+)/$', views.node_parent, name='node_parent'),
]
