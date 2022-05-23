from django.urls import path
from . import views


urlpatterns = [
    path('get_account_data', views.AccountView.as_view(), name='get_account_data')
]
