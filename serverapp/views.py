import json

from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.http import JsonResponse
from data_push.models import Account
from serverapp.services import WebHookProcess
from rest_framework.decorators import api_view


# Create your views here.

# class Server(View):

@api_view(['GET', 'POST'])
def json_handling(request):
    try:
        if request.method == 'GET' or type(request.data) is not dict:
            response_json = {'message': 'invalid_data'}
            return JsonResponse(response_json, status=422)
        elif request.method == 'POST':
            app_secret = request.headers.get('CL-X-TOKEN')
            if not app_secret:
                return HttpResponse('Unauthorized', status=401)
            account_ent = Account.objects.get(app_secret=app_secret)
            if not account_ent:
                return HttpResponse('Account not available', status=404)
            response = WebHookProcess.json_data_handler(account_ent, request.data)
            return HttpResponse('data pushed', status=200)
    except Exception as e:
        return HttpResponse('INTERNAL SERVER ERROR', status=500)
