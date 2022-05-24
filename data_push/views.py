import json
from django.shortcuts import render
from data_push.services import AccountSync

from django.http import HttpResponse
from django.http import JsonResponse
from django.views import View


class AccountView(View):
    def get(self, request, *args, **kwargs):
        try:
            response = AccountSync.get_account_data(request.GET.get('account_id'))
            return JsonResponse(response, status=200)
        except Exception as e:
            return HttpResponse('INTERNAL SERVER ERROR', status=500)

    def post(self, request, *args, **kwargs):
        try:
            print(request)
            data = json.loads(request.body.decode('utf-8'))
            response = AccountSync.save_account_data(data)
            return HttpResponse('INTERNAL SERVER ERROR', status=500)
            # response = AccountSync.get_account_data(request.POST.get('account_id'))
            # return JsonResponse(response, status=200)
        except Exception as e:
            return HttpResponse('INTERNAL SERVER ERROR', status=500)