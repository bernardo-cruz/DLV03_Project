#%%

import numpy as np
import matplotlib.pyplot as plt

class FunctionHelper:
    """This function creates functions and plots for a CNN function
    """
    def __init__(self, x_start:int, x_range:int, type:str,num:int=50):
        self.x_range = x_range
        self.x_start = x_start
        self.num = num
        self.__types = {'linear':self.linear,'quadratic':self.quadratic,'cubic':self.cubic}
        if type in self.__types:
            self.__type = type
        else:
            raise ValueError(f'{type} is not a valid function type')

    @property    
    def linear(self):
        self._y = self.x
        return self._y
    
    @property
    def quadratic(self):
        self._y = self.x**2
        return self._y
    
    @property
    def cubic(self):
        self._y = self.x**3
        return self._y

    @property
    def x(self):
        return np.linspace(start = self.x_start, stop = self.x_start + self.x_range,num=self.num)

    @property
    def y(self):
        return self.__types[self.__type]
    
    @property
    def plot(self):
        return plt.plot(self.x,self.y)

    def __str__(self):
        unit_vector_1 = self.x / np.linalg.norm(self.x)
        unit_vector_2 = self.y / np.linalg.norm(self.y)
        dot_product = np.dot(unit_vector_1, unit_vector_2)
        angle = np.round(np.arccos(dot_product),decimals=5)
        return f"FunctionHelper object | Type: {self.__type}"
    
    def __repr__(self):
        return self.__str__()
    
#%%

linear = FunctionHelper(x_start = 0, x_range = 10, type = 'linear')
#quadratic = FunctionHelper(x_start = 0, x_range = 10, type = 'quadratic')
#cubic = FunctionHelper(x_start = 0, x_range = 10, type = 'cubic')

# %%
