from utils.Receipt import *
from utils.singleton import Singleton


class display_board(Singleton):
    waitings = list()
    queue_size = 0

    def add_waiter(self, receipt):
        self.waitings.append(receipt.waiting_num)

    def delete_waiter(self, receipt):
        print self.waitings
        self.waitings.remove(receipt.waiting_num)

    def get_all_waiters(self):
        return self.waitings