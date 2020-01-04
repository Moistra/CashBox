from collections.abc import Iterable, Iterator
from typing import List
from Operation import Operation


class OperationsOrderIterator(Iterator):  # Релаизация конкретного итератора
    _position: int = None  # Текущее положение обхода
    _reverse: bool = False  # Направление обхода

    def __init__(self, collection, reverse: bool = False) -> None:
        self._collection = collection
        self._reverse = reverse
        self._position = -1 if reverse else 0

    def __next__(self):
        try:
            value = self._collection[self._position]
            self._position += -1 if self._reverse else 1
        except IndexError:
            raise StopIteration()

        return value


class OperationsCollection(Iterable):  # Коллекция для итерирования

    def __init__(self, collection: List[Operation] = []) -> None:
        self._collection = collection

    def __iter__(self) -> OperationsOrderIterator:
        return OperationsOrderIterator(self._collection)

    def get_reverse_iterator(self) -> OperationsOrderIterator:
        return OperationsOrderIterator(self._collection, True)

    def add_item(self, item: Operation):
        self._collection.append(item)
