#%%

import numpy as np
import matplotlib.pyplot as plt

class Functionbuilder:
    """
    This function creates functions and plots for a CNN function.
    """
    def __init__(self, x_start:int, x_range:int, num:int=50):
        self.x_range = x_range # range of x values
        self.x_start = x_start # start of x values
        self.num = x_start + x_range # number of x values
        self.type = 'Not defined'
        self.y_start = 'Not defined' # start of x values
        self.y_end = 'Not defined' # range of x values
        
    @property
    def x(self):
        return np.linspace(
            self.x_start, 
            self.x_start + self.x_range,
            self.num
            )
    
    # Create a linear function
    def linear(self, m=1,c=0):
        self.type = 'linear'
        self.m = m
        self.c = c
        self.y = self.m * self.x + self.c
        self.y_start = np.min(self.y)
        self.y_end = np.max(self.y)
        return self.y
    
    # Create a quadratic function
    def quadratic(self, c_1=0, c_2=0, c_0=0):
        self.type = 'quadratic'
        self.c_0 = c_0
        self.c_1 = c_1
        self.c_2 = c_2
        self.y = self.c_0 * self.x**0 + self.c_1 * self.x**2 + self.c_2 * self.x
        self.y_start = np.min(self.y)
        self.y_end = np.max(self.y)
        return self.y

    @property
    def plot(self):
        print('x is equal to:\n',self.x)
        print('y is equal to:\n',self.y)
        plt.rcParams["figure.figsize"] = (10,10)       
        plt.rcParams["lines.linewidth"] = 5
        plt.rcParams["axes.linewidth"] = 0
        plt.rcParams['axes.labelcolor'] = 'white'
        plt.show()
        plt.axis('off')
        return plt.plot(
            self.x,
            self.y,
            )

    def __str__(self):
        return f"""
        | Functionbuilder object: Type {self.type} |
        | x_start: {self.x_start} | x_end: {self.x_start+self.x_range} |
        | y_start: {self.y_start} | y_end: {self.y_end} |
        """

    def __repr__(self):
        return self.__str__()


# %%
