from typing import List


class Stack:
    """LIFO Queue implementation in Python

    Attributes:
    ----------
        items : List
            a list containing all items if the stack

    """

    __items: List = []

    def __len__(self) -> int:
        """Determines number of items in the stack

        Returns:
        -------
        int: Number of items in the stack
        """
        return len(self.__items)

    def __str__(self) -> str:
        """Prints the items of stack in readable format

        Returns:
        -------
        str: Items of stack
        """
        return str(self.__items)

    def __iter__(self) -> object:
        """Iterate through the items of the stack

        Yields:
        ------
        Generator[object]
        """
        for item in self.__items:
            yield item

    def push(self, item: object) -> None:
        """Add an item in the stack

        Parameters:
        ----------
        item : object
            The value item to add in the stack
        """
        self.__items.append(item)

    def pop(self) -> object:
        """Removes the last item added in the stack

        Raises:
        ------
        IndexError
            If no item is left to pop it raises index error 

        Returns:
        -------
        object: The last item added in the stack
        """
        if self.__len__() == 0:
            raise IndexError
        return self.__items.pop()
