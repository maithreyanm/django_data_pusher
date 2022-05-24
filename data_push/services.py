import uuid

from data_push.models import Account, Destination, HttpChoice


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
                                  app_secret=uuid.uuid4().hex, website=data['website'], email=data['email'])
            account_ent.save()
            if data.get('destinations'):
                for destination in data['destinations']:
                    headers_dict = {
                        "app_id": data['account_id'],
                        "app_secret": account_ent.app_secret,
                        "action": "user.create",
                        "Content-Type": "application/json",
                        "Accept":"*"

                    }
                    destination = Destination(url=destination['url'], http_method=destination['http_method'],
                                              headers=headers_dict, acc_key=account_ent)
                    destination.save()
            else:
                pass
            return {'account_id': account_ent.pid}

        except Exception as e:
            raise e

    @classmethod
    def update_account_data(cls, to_be_updated_data):
        try:
            account_ent = Account.objects.filter(account_id=to_be_updated_data['account_id'])[0]
            to_be_updated_data.pop('account_id')
            if account_ent:
                for k, v in to_be_updated_data.items():
                    exec(f"account_ent.{k}=\'{v}\'")
                    account_ent.save()
                    return True
            else:
                return False
        except Exception as e:
            raise e

    @classmethod
    def delete_account_data(cls, account_id):
        try:
            account_ent = Account.objects.filter(account_id=account_id)[0]
            if account_ent:
                account_ent.delete()
                return True
            else:
                return False
        except Exception as e:
            raise e


class DestinationSync:

    @classmethod
    def get_destination_data(cls, destination_entities):
        try:
            destination_list = []
            if len(destination_entities) > 0:
                for destination in destination_entities:
                    destination_response = {
                        'url': destination.url,
                        'http_method': destination.http_method,
                        'headers': destination.headers
                    }
                    destination_list.append(destination_response)
            return destination_list
        except Exception as e:
            raise e

    @classmethod
    def save_destination_data(cls, account_ent, data):
        try:
            destinations = data['destinations']
            for destination in destinations:
                destination = Destination(url=destination['url'], http_method=destination['http_method'],
                                          headers=destination['headers'], acc_key=account_ent)
                destination.save()
        except Exception as e:
            raise e
