#-*- coding: 949 -*-
from utils.singleton import Singleton
import abc


class menu_list(Singleton):
    menus = list()

    def add_menu(self, name, price, menu_type, origin_list=None):
        mdescription = menu_description(name, price, menu_type, origin_list)
        if mdescription is None:
            print "fail to add menus"
            return None

        mdict = dict()
        mdict['name'] = name
        mdict['menus'] = mdescription
        self.menus.append(mdict)

    def modify_menu(self, name, price):
        pass

    def get_all_menu(self):
        menu_des_list = list()
        for l in self.menus:
            menu_des_list.append(l['menus'])
        return menu_des_list

    def get_menu(self, name):
        selected_menu = None

        for m in self.menus:
            if m['name'] == name:
                selected_menu = m['menus']
                return selected_menu

        print "there is no " + name
        return None

    def delete_menu(self, name):
        for m in self.menus:
            print str(type(str(m['name'].encode('utf-8')))) + " " + m['name']
            if str(m['name']) == str(name):
                del m


class menu_description:
    name = None
    price = None
    menu_type = None
    origin_list = None

    def __init__(self, name, price, menu_type, origin_list=None):
        self.name = name
        self.price = price

        if not self.check_type(menu_type) is None:
            self.menu_type = menu_type
        else:
            print "menu_description.__init__ : " + name + " invalid type : " + menu_type
            return

        self.origin_list = origin_list

    def check_type(self, menu_type):
        str_menu_type = str(menu_type)
        if not ((str_menu_type == "main") or (str_menu_type == "sub")):
            return None
        return str_menu_type


class menu_base:
    name = None
    selected_menu = None
    menu_list = menu_list()
    # total_price

    @abc.abstractmethod
    def discount(self):
        return


class main_menu(menu_base):
    def __init__(self, name):
        self.name = name
        self.selected_menu = self.menu_list.get_menu(name)

        if self.selected_menu is None:
            print "sub_menu.__init__ : There is no mene name : " + name
            return

        if self.selected_menu.menu_type is "main":
            self.menu_type = "main"
        else:
            print "main_menu.__init__ : invalid menus type"
            return

        self.price = self.selected_menu.price

    def discount(self):
        return self.price


class sub_menu(menu_base):
    def __init__(self, name):
        self.name = name
        self.selected_menu = self.menu_list.get_menu(name)

        if self.selected_menu is None:
            print "sub_menu.__init__ : There is no mene name : " + name
            return

        if self.selected_menu.menu_type is "sub":
            self.menu_type = "sub"
        else:
            print "sub_menu.__init__ : " + self.name + " invalid menus type"
            return

        self.price = self.selected_menu.price
        self.price = self.discount()
        print self.selected_menu.price

    def discount(self):
        return self.price / 2