from collections import deque
from typing import Deque

class Queue:
    """FIFO Queue implementation in Python

    Attributes:
    ----------
        items : deque
            a double ended queue containing all items in the queue

    """
    __items: Deque = deque()

    def __len__(self) -> int:
        """Determines number of items in the queue

        Returns:
        -------
        int: Number of items in the queue
        """
        return len(self.__items)

    def __str__(self) -> str:
        """Prints the items of queue in readable format

        Returns:
        -------
        str: Items of queue
        """
        return str(self.__items)

    def __iter__(self) -> object:
        """Iterate through the items of the queue

        Yields:
        ------
        Generator[object]
        """
        for item in self.__items:
            yield item

    def push(self, item: object) -> None:
        """Add an item in the queue

        Parameters:
        ----------
        item : object
            The value item to add in the queue
        """
        self.__items.append(item)

    def pop(self) -> object:
        """Removes the first item added in the queue

        Raises:
        ------
        IndexError
            If no item is left to pop it raises index error

        Returns:
        -------
        object: The first item added in the queue
        """
        if self.__len__() == 0:
            raise IndexError
        return self.__items.popleft()
