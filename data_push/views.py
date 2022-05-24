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
            data = json.loads(request.body.decode('utf-8'))
            response_dict = AccountSync.save_account_data(data)
            return JsonResponse(response_dict, status=200)
        except Exception as e:
            return HttpResponse('INTERNAL SERVER ERROR', status=500)

    def patch(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body.decode('utf-8'))
            account_id = data['account_id']
            isUpdated = AccountSync.update_account_data(data)
            if isUpdated:
                return HttpResponse(f'udpated account for account_id: {account_id}', status=200)
            else:
                return HttpResponse(f'account for account_id: {account_id} not found', status=404)
        except Exception as e:
            return HttpResponse('INTERNAL SERVER ERROR', status=500)

    def delete(self, request, *args, **kwargs):
        try:
            account_id = json.loads(request.body.decode('utf-8')).get('account_id')
            is_deleted = AccountSync.delete_account_data(account_id)
            if is_deleted:
                return HttpResponse(f'deleted account for account_id: {account_id}', status=200)
            else:
                return HttpResponse('record not found or already deleted', 404)
        except Exception as e:
            return HttpResponse('INTERNAL SERVER ERROR', status=500)