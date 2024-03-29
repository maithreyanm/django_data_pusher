from django.urls import path
from . import views


urlpatterns = [
    path('get_account_data', views.AccountView.as_view(), name='get_account_data'),
    path('save_account_data', views.AccountView.as_view(), name='save_account_data'),
    path('update_account_data', views.AccountView.as_view(), name='update_account_data'),
    path('delete_account_data', views.AccountView.as_view(), name='delete_account_data'),
    path('get_destination_data', views.DestinationView.as_view(), name='get_account_data'),
    path('post_destination_data', views.DestinationView.as_view(), name='post_account_data'),
    path('update_destination_data', views.DestinationView.as_view(), name='update_account_data'),
    path('delete_destination_data', views.DestinationView.as_view(), name='delete_account_data')
]