from abc import ABC, abstractmethod
from Windows import *


class Creator(ABC):
    @abstractmethod
    def factory_method(self, view):
        pass


class MainWindowCreator(Creator):
    def factory_method(self, view) -> MainWindow:
        return MainWindow(view=view)


class SelectWindowCreator(Creator):
    def factory_method(self, view) -> AddOperationWindow:
        return AddOperationWindow(view=view)


