#%%

import numpy as np
import matplotlib.pyplot as plt

class Functionbuilder:
    """ This class creates dummy data and plot for later use in the CNN
    """
    def __init__(self, x_start:int, x_end:int, num:int=100):
        """[summary]

        Args:
            x_start (int): [start values of series]
            x_end (int, optional): [end values of series].
            num (int, optional): [number of interpolated values]. Defaults to 1000.
        """
        self.x_start = x_start # start of x values
        self.x_end = x_end # end of x values
        self.num = num # number of x values
        self.type = 'Not defined' # type of function
        self.y_start = 'Not defined' # start of x values
        self.y_end = 'Not defined' # range of x values
        
    @property
    def x(self):
        """Definition of x values as vector.

        Returns:
            [array]:[float values]
        """
        return np.linspace(
            self.x_start, 
            self.x_end,
            self.num
            )
    
    # Create a linear function
    def linear(self, m=1,c=0, scale = None):
        """ This method creates a linear function with slope m and intercept c.

        Args:
            m (int, optional): Slope of curve. Defaults to 1.
            c (int, optional): Offset of curve. Defaults to 0.

        Raises:
            ValueError: In case m and c are zero.

        Returns:
            [array]:[float values]
        """
        self.type = 'linear'
        if m == 0 and c == 0:
            raise ValueError('Linear function cannot be m = 0 and c = 0')
        self.m = m
        self.c = c
        self.y = self.m * self.x + self.c
        self.y_start = np.min(self.y)
        self.y_end = np.max(self.y)
        return self.y
    
    # Create a quadratic function
    def polynomial(self, coefficients:list=[0,0,0.01]):
        """This method creates a quadratic function with coefficients.

        Args:
            coefficients (list, optional): 
            The list coefficients of the polynom in the form [a,b,...,n] for [x**0,x**1,...,x**n].
            Defaults to [0,0,1].

        Raises:
            ValueError: In case coefficients is empty.

        Returns:
            [array]:[float values]
        """
        self.type = f'polynomial {len(coefficients)}'
        self.y = 0
        if coefficients:
            for i,c in enumerate(coefficients):
                setattr(self, f'c_{i}', c)
                self.y += c * self.x**i
        else:
            raise ValueError('No coefficients defined')
        self.y_start = np.min(self.y)
        self.y_end = np.max(self.y)
        return self.y

    # Create a exponential function
    def exponential(self, a = 1, b = 0.05, c = 0):
        """This method creates an exponential function with coefficients. The function is:
                a * exp(b * x) + c

        Args:
            a (int, optional): Defaults to 1.
            b (int, optional): Defaults to 1.
            c (int, optional): Defaults to 0.

        Returns:
            float: Vector of y values.
        """
        self.type = 'exponential'
        self.a = a
        self.b = b
        self.c = c
        self.y = self.a * np.exp(self.b * self.x) + self.c
        self.y_start = np.min(self.y)
        self.y_end = np.max(self.y)
        return self.y
    
    # Create a sinus function
    def sinus(self, a = 25, f = 0.5, o = 50):
        """This method creates a sinus function with coefficients. The function is:
                a * sin(b * x) + c

        Args:
            a (int, optional): Defaults to 1.
            f (int, optional): Defaults to 1.
            o (int, optional): Defaults to 0.

        Returns:
            float: Vector of y values.
        """
        self.type = 'sinus'
        self.a = a
        self.f = f
        self.o = o
        self.y = self.a * np.sin(self.f * self.x) + self.o
        self.y_start = np.min(self.y)
        self.y_end = np.max(self.y)
        return self.y
    
        # Adding Noise
    
    @property
    def noise(self):
        pass

    # Plot the function
    def plot(self, width = 10, height = 10):
        plt.rcParams["figure.figsize"] = (width,height)       
        plt.rcParams["lines.linewidth"] = 2
        plt.rcParams["axes.linewidth"] = 0.5
        plt.rcParams["axes.linewidth"] = 0.5
        plt.show()
        plt.figure()
        plt.xlim([self.x_start, self.x_end])
        #plt.ylim([self.x_start, self.x_end])
        plt.xticks([])
        plt.yticks([])
        plt.title(f'{self.type} function'.title()) # Add coefficients to title?????
        #plt.axis('off')
        return plt.plot(
            self.x,
            self.y,
            )

    # string representation of the object
    def __str__(self):
        return f"""
        | Functionbuilder object: Type {self.type} |
        | x_start: {self.x_start} | x_end: {self.x_end} |
        | y_start: {self.y_start} | y_end: {self.y_end} |
        """

    # repr of the object
    def __repr__(self):
        return self.__str__()


def coefficient_generator(mu = 1, sigma = None):
    if sigma == None:
        sigma = mu / 2    
    return sigma * np.random.randn() + mu

# %%

def test():
    x_start = 0
    x_end = 100
    num = 1000

    # Initialize the functionbuilder object
    function = Functionbuilder(x_start = x_start, x_end = x_end, num = num)

    # 
    function.linear(m = coefficient_generator(), c = coefficient_generator())
    function.plot()

    # 
    function.polynomial()#[1,0,1])
    function.plot()

    # 
    function.exponential(a = 1, b = 0.05, c = 0)
    function.plot()

    # 
    function.sinus(a = 25, f = 0.09, o = 50)
    function.plot()

test()
# %%
