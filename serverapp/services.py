import requests
from data_push.models import Account, Destination


class CustomException(Exception):
    pass


class WebHookProcess:

    @classmethod
    def json_data_handler(cls, account_ent, data):
        try:
            destination_entities = Destination.objects.all().filter(acc_key=account_ent.pid)
            for destination in destination_entities:
                if destination.http_method == 'GET':
                    query_param = data
                    response = APICall.call_api(method=destination.http_method, url=destination.url,
                                                headers=destination.headers, query_data=query_param)
                elif destination.http_method in ['POST', 'PUT']:
                    response = APICall.call_api(method=destination.http_method, url=destination.url,
                                                headers=destination.headers, body_data=data)
                else: pass

        except Exception as e:
            raise e


class APICall:
    @classmethod
    def call_api(cls, method, url, headers, query_data=None, body_data=None):
        try:
            if method == 'GET':
                response = requests.get(headers=headers, url=url, params=query_data)
            elif method == 'POST':
                response = requests.post(headers=headers, url=url, data=body_data)
            elif method == 'PUT':
                response = requests.patch(headers=headers, url=url,data=body_data)
            else:
                raise CustomException('wrong method or no method')

            return response
        except Exception as e:
            print(e)
