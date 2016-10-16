from django.conf.urls import url

from .views.login import LoginView
from .views.logout import LogoutView
from .views.register import RegisterView

urlpatterns = [
	url(r'^in/$', LoginView.as_view(), name='in'),
	url(r'^out/$', LogoutView.as_view(), name='out'),
	url(r'^register/$', RegisterView.as_view(), name='register'),
]