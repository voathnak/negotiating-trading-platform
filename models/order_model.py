from snail.Model import CoreModel


class OrderModel(CoreModel):

    _required_fields = [
        'stock',
        'type',
        'username',
        'price',
        'quantity',
    ]

    def __init__(self, table_name):
        super(OrderModel, self).__init__(table_name)
