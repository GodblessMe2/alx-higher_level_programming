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
    
    def area(self):
        """calculates the square's area

        Returns:
            The area of the square
        """
        return (self.__size) ** 2
    
    @property
    def size(self):
        """Getter of __size
        
        Returns:
            The size of the square
        """
        return self.__size
    
    @size.setter
    def size(self, value):
        """Setter of __size
        
        Args:
           Value (int): the size of a size of the square
        
        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
