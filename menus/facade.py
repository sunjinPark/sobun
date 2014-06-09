from menus import menu


class menu_facade:
    #CRUD
    #logging
    facade = menu.menu_list()

    def create_menu(self, name, price, menu_type, origin_list=None):
        operation = "Create menu : " + name + " "
        self.facade.add_menu(name, price, menu_type, origin_list)

    def get_menu(self, name):
        operation = "Get menu : " + name + " "
        selected_menu = self.facade.get_menu(name)
        return selected_menu

    def get_all_menu(self):
        operation = "Get All "
        menu_list = self.facade.get_all_menu()
        return menu_list

    def update_menu(self):
        pass

    def delete_menu(self, name):
        operation = "Delete Menu : " + name + " "
        self.facade.delete_menu(name)

    def delete_all(self):
        pass