import json

from snail.Model import CoreModel


class UserModel(CoreModel):

    _required_fields = ['fullname', 'email', 'username', 'password']

    username = None
    fullname = None
    cash_balance = 0
    stock_balance = None
    email = None

    def __init__(self, table_name):
        super(UserModel, self).__init__(table_name)

    def save(self, values):
        values.update({
            'itemId': values.get('email'),
            'fullname': "{} {}".format(values.get('firstName'), values.get('lastName')),
            'cash_balance': 0,
            'stock_balance': {}
        })
        return super(UserModel, self).save(values)
