from django.urls import path
from . import views


urlpatterns = [
    path('incoming_data', views.Server.as_view(), name='incoming_data'),
]