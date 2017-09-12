
from models.base import Base


class Rectangle(Base):
    """ Rectangle class interated from ``Base`` class """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initilizes and sets respective attributes """

        super().__init__(id)  # calls Base class and sets id according to rules
        #  class respective methods to set values
        self.width, self.height, self.x, self.y = width, height, x, y

# ------ Getters and Setters ---------
    @property
    def width(self):
        """
        Width attribute getter and setter
        Raises:
            TypeError: width not int
            ValueError: width <= 0
        """
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """
        Height attribute getter and setter
        Raises:
            TypeError: height not int
            ValueError: height <= 0
        """
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """
        x attribute getter and setter
        Raises:
            TypeError: x not int
            ValueError: x < 0
        """
        return self.__x

    @x.setter
    def x(self, x):
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """
        y attribute getter and setter
        Raises:
            TypeError: y not int
            ValueError: y < 0
        """
        return self.__y

    @y.setter
    def y(self, y):
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

# -------- Specilized methods ------------

    def area(self):
        """ Returns: width * height """

        return self.__width * self.__height

    def display(self):
        """ Print visual representation of Rectange according to position"""

        [print() for y in range(self.__y)]  # Y position
        # X position then print
        [print(' ' * self.__x, '#' * self.__width, sep='')
            for i in range(self.__height)]

    def __str__(self):
        """ Returns: [Rectangle] (id) x/y - width/height """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """ Updates attributes in class Rectangle """
        if len(args):  # if args is passed
            RecAttr = iter(['width', 'height', 'x', 'y'])  # iter for next()
            for idx, arg in enumerate(args):
                if idx == 0:  # handles id
                    super().__init__(arg)  # calls Bases Intit
                    continue
                try:  # argument validation
                    # calls respective setter method
                    setattr(self, next(RecAttr), arg)
                except Exception as error:  # setter error msg
                    print(error)
        else:  # if kwargs is passed
            for key, value in kwargs.items():
                if key == id:  # handles id
                    super().__init__(key)  # calls Bases intit
                    continue
                if hasattr(self, key):  # key validation
                    try:  # argument validation
                        # calls respective setter method
                        setattr(self, key, value)
                    except Exception as error:  # setter error msg
                        print(error)
                else:  # if key doesnt exist dont create attribute
                    continue

    def to_dictionary(self):
        """ Returns: dict of instances attributes """
        RecAttr = ['id', 'width', 'height', 'x', 'y']  # get following attr
        newdict = {attr: getattr(self, attr) for attr in RecAttr}
        return newdict
