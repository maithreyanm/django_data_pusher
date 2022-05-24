from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.http import JsonResponse
from data_push.models import Account
from serverapp.services import WebHookProcess


# Create your views here.

class Server(View):

    def get(self, request, *args, **kwargs):
        try:
            app_secret = request.json.get('app_secret')
            if not app_secret:
                return HttpResponse('Unauthorized', status=401)
            account_ent = Account.objects.get(app_secret=app_secret)
            if not account_ent:
                return HttpResponse('Account not available', status=404)
            response = WebHookProcess.json_data_handler(account_ent)
            return JsonResponse('ok', status=200)
        except Exception as e:
            return HttpResponse('INTERNAL SERVER ERROR', status=500)
