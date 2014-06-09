from kitchens import kitchen
from stores import order
from clients import display_board
from menus.menu import main_menu
from utils import Receipt


class kitchen_facade:
    kitchen = kitchen.cook_manager()
    order_manager = order.order_manager()
    display = display_board.display_board()

    def cook_finished(self, num):

        finish_receipt = self.kitchen.alarm_to_client(num)
        self.display.add_waiter(finish_receipt)

        #connect to push server
        #logging
        return finish_receipt

    def take_cook(self):
        self.kitchen.finish_cook()
        target_receipt = self.order_manager.finish_order()
        self.display.delete_waiter(target_receipt)
        #logging
        return None

    def get_all_cook_list(self):
        cook_list = self.kitchen.get_all_cook_list()
        #logging
        return cook_list

