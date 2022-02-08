#Position.py

import constants

class Position():

    #constructor
    def __init__(self, x, y):

        #check for valid parameters
        if (isinstance)(x, float):
            x = int(x)
        if not isinstance(x, int):
            raise TypeError(f"Argument x must be of type int, not {type(x)} x:{x}")
        if (isinstance)(y, float):
            y = int(y)
        if not isinstance(y, int):
            raise TypeError(f"Argument y must be of type int, not {type(y)} y:{y}")
#        if x < 0 or x > constants.FRAME_MAX_X:
#            raise ValueError(f"Argument x must be between 0 and {constants.FRAME_MAX_X} x:{x}")
#        if y < 0 or y > constants.FRAME_MAX_Y:
#            raise ValueError(f"Argument y must be between 0 and {constants.FRAME_MAX_Y} y:{y}")

        self.x = x
        self.y = y

    def __str__(self):
        return f'x:{self.x} y:{self.y}'

    # This method gets called when using == on the object
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y