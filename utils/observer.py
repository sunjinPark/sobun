import abc


class Observer:
    @abc.abstractmethod
    def update(self, obj):
        return


class Watcher:
    @abc.abstractmethod
    def notifyObservers(self, obj):
        return

    @abc.abstractmethod
    def registerObserver(self, observer):
        return

    @abc.abstractmethod
    def removeObserver(self, observer):
        return


class Subject(object):
    @abc.abstractmethod
    def action(self):
        return