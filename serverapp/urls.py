from django.urls import path
from . import views


urlpatterns = [
    path('incoming_data', views.incoming_data, name='incoming_data'),
]