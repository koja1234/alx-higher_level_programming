#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Tue July 19 23:28:24 2022
@author: Kassim Juma Amir
"""


class Square:
    """Class Square that has attributes. Instantiation with size
    Attributes:
        size (int): The size of the square
    """

    def __init__(self, size):
        """The __init__ method for Square class
        Args:
            size: (:obj: 'int'): A private instance size
        """
        self.__size = size
