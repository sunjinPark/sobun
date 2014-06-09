import string
import random
import datetime


class Receipt:
    menu = None
    random_string = None
    waiting_num = None
    order_date = None

    def __init__(self, menu, waiting_num):
        self.menu = menu
        self.waiting_num = waiting_num
        self.random_string = self.__generate_random_string()
        self.order_date = datetime.datetime.now()

    def __generate_random_string(self):
        size = 20
        allowed = string.ascii_letters
        randomstring = ''.join([allowed[random.randint(0, len(allowed)-1)] for x in xrange(size)])
        return randomstring




