from django.urls import path
from . import views


urlpatterns = [
    path('incoming_data', views.json_handling, name='incoming_data'),
]