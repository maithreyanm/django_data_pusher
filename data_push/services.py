from data_push.models import Account


class AccountSync:

    @classmethod
    def get_account_data(cls, account_id):
        try:
            account = Account.objects.get(account_id=account_id)
            return account.__dict__
        except Exception as e:
            print(e)
