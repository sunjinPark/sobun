import abc
from menus.menu import *
from stores.order import *
from utils.Receipt import Receipt


class Store_base:
    order_manager = order_manager()
    menu = None

    @abc.abstractmethod
    def create_menu(self, menu_type, menu_name):
        return

    def make_receipt(self, menu):
        waiting_num = self.order_manager.get_waiting_num()
        return Receipt(menu, waiting_num)

    def order_menu(self, menu_type, menu_name):
        menu = self.create_menu(menu_type, menu_name)
        receipt = self.make_receipt(menu)
        self.order_manager.add_order(receipt)

        return receipt


class Paldal(Store_base):
    def create_menu(self, menu_type, menu_name):
        if menu_type == "main":
            menu = main_menu(menu_name)
            return menu

        elif menu_type == "sub":
            menu = sub_menu(menu_name)
            return menu




