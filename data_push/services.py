from data_push.models import Account, Destination


class AccountSync:

    @classmethod
    def get_account_data(cls, account_id):
        try:
            account_ent = Account.objects.get(account_id=account_id)
            destination_entities = Destination.objects.all().filter(acc_key=account_ent.pid)
            destination_list = []
            for destination in destination_entities:
                destination_response = {
                    'url': destination.url,
                    'http_method': destination.http_method,
                    'headers': destination.headers
                }
                destination_list.append(destination_response)
            response_payload = {
                'account_name': account_ent.account_name,
                'account_id': account_ent.account_id,
                'web_site': account_ent.website,
                'destinations': destination_list
            }
            return response_payload
        except Exception as e:
            raise e

    @classmethod
    def save_account_data(cls, data):
        try:
            account_ent = Account(account_name=data['account_name'], account_id=data['account_id'],
                                  app_secret=data['app_secret'], website=data['website'])
            account_ent.save()
            for destination in data['destinations']:
                destination = Destination(url=destination['url'], http_method=destination['http_method'], headers=destination['headers'])
            destination.save()
        except Exception as e:
            raise e
