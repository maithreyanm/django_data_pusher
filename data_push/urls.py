from django.urls import path
from . import views


urlpatterns = [
    path('get_account_data', views.AccountView.as_view(), name='get_account_data'),
    path('save_account_data', views.AccountView.as_view(), name='save_account_data'),
    path('update_account_data', views.AccountView.as_view(), name='update_account_data')
]