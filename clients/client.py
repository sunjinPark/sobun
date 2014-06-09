import abc


class client_facade:
    @abc.abstractmethod
    def order_menu(self):
        pass

    @abc.abstractmethod
    def take_menu_list(self):
        pass

    @abc.abstractmethod
    def take_menu(self):
        pass


class android_facade(client_facade):
    pass