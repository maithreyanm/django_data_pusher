import json
from django.shortcuts import render

from data_push.models import Account, Destination
from data_push.services import AccountSync, DestinationSync

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


class DestinationView(View):
    def get(self, request, *args, **kwargs):
        try:
            account_ent = Account.objects.get(account_id=request.GET.get('account_id'))
            destination_entities = Destination.objects.all().filter(acc_key=account_ent.pid)
            if not account_ent:
                return HttpResponse(f'No destination data for the {request.GET.get("account_id")}', 404)
            destination_payload_list = DestinationSync.get_destination_data(destination_entities)
            response = {'account_id': request.GET.get('account_id'), 'destinations': destination_payload_list}
            return JsonResponse(response, status=200)
        except Exception as e:
            return HttpResponse('INTERNAL SERVER ERROR', status=500)

    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body.decode('utf-8'))
            account_ent = Account.objects.get(account_id=data['account_id'])
            if not account_ent:
                return HttpResponse(f'cannot save destination due to unavailability of account', 404)
            DestinationSync.save_destination_data(account_ent, data)
            return HttpResponse(f'saved destination data against account: {data["account_id"]}', 201)
        except Exception as e:
            return HttpResponse('INTERNAL SERVER ERROR', status=500)
