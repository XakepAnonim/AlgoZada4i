class Test:

    # def __init__(self, name):
    #     self.name = name
    #
    # def __repr__(self):
    #     return 'Object Test'
    #
    # def __str__(self):
    #     return f'Наименование товара {self.name}'
    def __bool__(self):
        return 2 < 6


t = Test()
# t2 = Test('phone')
if t:
    print('fsdfsfds')