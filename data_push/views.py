from django.shortcuts import render
from data_push.services import AccountSync

from django.http import HttpResponse
from django.views import View


class AccountView(View):
    def get(self, request, *args, **kwargs):
        acc_name = AccountSync.get_account_data(request.GET.get('account_id'))
        return HttpResponse(acc_name)
