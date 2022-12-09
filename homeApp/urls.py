from django.urls import path
from homeApp.views import *

urlpatterns = [
	path('', home, name='home')
]