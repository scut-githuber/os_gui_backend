from django.conf.urls import url

from . import views

urlpatterns = [
    # example:
    # url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^register/$', views.register, name='register'),
    url(r'^node_child/(?P<node_id>[0-9]+)/$', views.node_child, name='node_child'),
    url(r'^node_brother/(?P<node_id>[0-9]+)/$', views.node_brother, name='node_brother'),
    url(r'^node_parent/(?P<node_id>[0-9]+)/$', views.node_parent, name='node_parent'),
    url(r'^create_node/(?P<node_type>[0-9]+)/(?P<root_id>[0-9]+)/$', views.create_node, name='create_node'),
    url(r'^remove_node/(?P<project_id>[0-9]+)/(?P<id_on_tree>[0-9]+)/$', views.remove_node, name='remove_node'),
    url(r'^alter_node/(?P<node_id_alter>[0-9]+)/(?P<node_id_connect>[0-9]+)/(?P<ref_type>[0-2]+)/$', views.alter_node, name='alter_node'),
    url(r'^new_project/(?P<node_type>[0-9]+)/(?P<name>[0-9|a-z]+)/(?P<user_id>[0-9]+)/$', views.new_project, name='new_project'),
    url(r'^node_connect/(?P<node_id_a>[0-9]+)/(?P<node_id_b>[0-9]+)/(?P<ref_type>[0-2]+)/$', views.node_connect, name='node_connect'),
    url(r'^init_rel/', views.init_rel, name='init_rel')
]
