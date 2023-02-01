import numpy as np
from random import choice

class Gradient:

    def create_gradient(self, start, stop, width, height, direction):
        # if direction True is horisontal else vertical
        if direction:
            return np.tile(np.linspace(start, stop, width), (height, 1))
        else:
            return np.tile(np.linspace(start, stop, height), (width, 1)).T

    def image(self, size: tuple, start_color: tuple, end_color: tuple):
        width, height = size
        list_direction_gradient = [choice([True, False]) for i in range(3)]
        # list_direction_gradient = (True, False, True)
        result = result = np.zeros((height, width, len(start_color)), dtype=np.cfloat)

        for i, (start, stop, is_horizontal) in enumerate(zip(start_color, end_color, list_direction_gradient)):
            result[:, :, i] = self.create_gradient(start, stop, width, height, is_horizontal)

        return result
