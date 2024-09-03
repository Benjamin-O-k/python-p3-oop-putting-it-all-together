#!/usr/bin/env python3

class Shoe:
    def __init__(self,brand,size):
        self.brand = brand
        self.size = size
        self._condition = None

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            print("size must be an integer")
            return
        self.__size = size

    @property
    def condition(self):
        return self._condition

    def cobble(self):
        print("Your shoe is as good as new!")
        self._condition = "New"
