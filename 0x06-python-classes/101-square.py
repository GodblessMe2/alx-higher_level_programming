#!/usr/bin/python3
"""Define the class Square"""

class Square:
    """Represents a square
    
    Attributes:
        __size (int): size of the square
        __position (tuple): position of the square in 2D space
    """
    def __init__(self, size=0, position=(0,0)):
        """Initializing the square
        Args:
           size (int): size of a side of the square
        
        Returns:
            None
        """
        self.__size = size
        self.__position = position
    
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
    
    def my_print(self):
        """Print the square
        
        Returns:
            None
        """
        if self.__size == 0:
            print()
            return
        for l in range(self.__position[1]):
            print()
        for i in range(self.__size):
            print("".join([" " for k in range(self.__position[0])]), end="")
            print("".join(["#" for j in range(self.__size)]))
    
    @property
    def position(self):
        """Getter of __position
        
        Returns:
            The position of the square
        """
        return self.__position
    
    @position.setter
    def position(self, value):
        """Setter of __position
        
        Args:
           Value (tuple): the position of the square in 2D space
        
        Returns:
            None
        """
        if type(value) is not tuple or len(value) != 2 or \
           type(value[0]) is not int or value[0] < 0 or \
           type(value[1]) is not int or value[1] < 0:
           raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
    
    def __str__(self):
        """String representing the square instance
        
        Returns:
            Formatted string representing the square
        """
        if self.size == 0:
            return ""
        string = "\n" * self.position[1] + (" " * self.position[0]
                                           + "#" * self.size + "\n") * self.size
        return string[:-1]
        