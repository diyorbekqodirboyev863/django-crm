# urls.py

from django.urls import path
from . import views

urlpatterns = [
	path(route='', view=views.index, name='index'),
	path(route='logout/', view=views.logout_user, name='logout'),
	path(route='register/', view=views.register_user, name='register'),
]