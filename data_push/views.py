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
            response = AccountSync.get_account_data(request.GET.get('email'))
            return JsonResponse(response, status=200)
        except Exception as e:
            return HttpResponse('INTERNAL SERVER ERROR', status=500)

    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body.decode('utf-8'))
            account_ent_email = Account.objects.all().filter(email=data['email'])
            account_ent_id = Account.objects.all().filter(account_id=data['account_id'])
            if len(account_ent_email) != 0:
                return HttpResponse(f'account already exists with email: {data["email"]}', status=500)
            if len(account_ent_id) != 0:
                return HttpResponse(f'account already exists with acc id: {data["account_id"]}', status=500)
            response_dict = AccountSync.save_account_data(data)
            return JsonResponse(response_dict, status=200)
        except Exception as e:
            return HttpResponse('INTERNAL SERVER ERROR', status=500)

    def patch(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body.decode('utf-8'))
            email = data['email']
            isUpdated = AccountSync.update_account_data(data)
            if isUpdated:
                return HttpResponse(f'udpated account for email: {email}', status=200)
            else:
                return HttpResponse(f'account for email: {email} not found', status=404)
        except Exception as e:
            return HttpResponse('INTERNAL SERVER ERROR', status=500)

    def delete(self, request, *args, **kwargs):
        try:
            email = json.loads(request.body.decode('utf-8')).get('email')
            is_deleted = AccountSync.delete_account_data(email)
            if is_deleted:
                return HttpResponse(f'deleted account for email: {email}', status=200)
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
            account_ent = Account.objects.all().filter(email=data['email'])
            if not account_ent:
                return HttpResponse(f'cannot save destination due to unavailability of account', 404)
            DestinationSync.save_destination_data(account_ent, data)
            return HttpResponse(f'saved destination data against account: {data["account_id"]}', 201)
        except Exception as e:
            return HttpResponse('INTERNAL SERVER ERROR', status=500)

    def delete(self, request, *args, **kwargs):
        try:
            email = json.loads(request.body.decode('utf-8')).get('email')
            is_deleted = DestinationSync.delete_destination_data(email)
            if is_deleted:
                return HttpResponse(f'deleted destination for email: {email}', status=200)
            else:
                return HttpResponse('record not found or already deleted', 404)
        except Exception as e:
            return HttpResponse('INTERNAL SERVER ERROR', status=500)
