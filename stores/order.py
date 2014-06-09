from utils.singleton import Singleton
from utils.observer import *


class order_manager(Singleton, Watcher):
    receipt_list = list()
    waiting_num = None
    observers = list()

    def __init__(self):
        self.waiting_num = 1

    def add_order(self, receipt):
        self.receipt_list.append(receipt)
        self.waiting_num += 1
        self.notifyObservers(receipt)

    def get_all_order_list(self):
        return self.receipt_list

    def finish_order(self):
        removed_num = self.receipt_list[0]
        self.receipt_list.pop(0)
        return removed_num

    def get_all_menu(self):
        menu_des_list = list()
        for l in self.receipt_list:
            menu_des_list.append(l['menus'])
        return menu_des_list

    def get_waiting_num(self):
        return self.waiting_num

    def alarm_to_client(self):
        pass

    def notifyObservers(self, obj):
        for o in self.observers:
            o.update(obj)
        return

    def registerObserver(self, observer):
        self.observers.append(observer)
        return

    def removeObserver(self, observer):
        self.observers.remove(observer)
        return
