from snail.Model import CoreModel


class TodoModel(CoreModel):

    def __init__(self, table_name):
        super(TodoModel, self).__init__(table_name)

    def save(self, values):
        return super(TodoModel, self).save(values)

