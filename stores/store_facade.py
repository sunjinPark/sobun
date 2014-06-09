from stores import store, order
from menus import menu
from clients import display_board


class store_facade:
    menus = menu.menu_list()
    order = order.order_manager()
    store = store.Paldal()
    display = display_board.display_board()

    def order_menu(self, menu_type, menu_name):
        order_receipt = self.store.order_menu(menu_type, menu_name)
        #logging

    def get_all_menu(self):
        order_list = self.order.get_all_order_list()
        #logging
        return order_list

    def show_all_menu_list(self):
        menu_list = self.menus.get_all_menu()
        return menu_list