#!/usr/bin/python3
"""Define the class Square"""


class Square:
    """Represents a square
    Attributes:
        __size (int): size of the square
    """
    def __init__(self, size=0):
        """Initializing the square
        Args:
           size (int): size of a side of the square
        Returns:
            None
        """
        self.__size = size
    """Area The square"""
    def area(self):
        """calculates the square's area
        Returns:
            The area of the square
        """
        return (self.__size) ** 2
    """property Getter"""
    @property
    def size(self):
        """Getter of __size
        Returns:
            The size of the square
        """
        return self.__size
    """Setter"""
    @size.setter
    def size(self, value):
        """Setter of __size
        Args:
           Value (int): the size of a size of the square
        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("size must be an number")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
    """Compare"""
    def __com__(self, other):
        """Compare the square is less than to the area
        Args:
           Other (square): square to compare against
        Returns:
            True or False
        """
        return self.size < other.size
    """Square Compare"""
    def __le__(self, other):
        """Compare if square is less than or equal to the area
        Args:
            Other (Square): square to compare against
        Returns:
            True or False
        """
        return self.size <= other.size
    """Square Compare"""
    def __eq__(self, other):
        """Compare if square is equal to the area
        Args:
            Other (Square): square to compare against
        Returns:
            True or False
        """
        return self.size == other.size
    """Square Compare"""
    def __ne__(self, other):
        """Compare if square is not equal to the area
        Args:
            other (Square): square to compare against
        Returns:
            True or False
        """
        return self.size != other.size
    """Square Compare"""
    def __ge__(self, other):
        """Compare if square is greater than or equal to the area
        Args:
            other (Square): square to compare against
        Returns:
            True or False
        """
        return self.size >= other.size
    """Square Compare"""
    def __gt__(self, other):
        """Compare if square is greater than the area
        Args:
            other (Square): square to compare against
        Returns:
            True or False
        """
        return self.size > other.size
