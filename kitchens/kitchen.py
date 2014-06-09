from utils.observer import *
from utils.singleton import *


class cook_manager(Singleton, Observer, Subject):
    watcher = None
    cook_list = list()

    def __init__(self, watcher=None):
        self.watcher = watcher
        if not watcher is None:
            watcher.registerObserver(self)

    def get_all_cook_list(self):
        return self.cook_list

    def add_cook(self, receipt):
        self.cook_list.append(receipt)

    def update(self, receipt):
        self.add_cook(receipt)
        self.action()
        return

    def action(self):
        #refresh
        print "page refresh"
        return

    def finish_cook(self):
        self.__remove_cook()
        return

    def __remove_cook(self):
        removed_num = self.cook_list[0]
        self.cook_list.pop(0)
        return removed_num

    def alarm_to_client(self, unum):
        num = int(unum)
        return self.cook_list[num-1]