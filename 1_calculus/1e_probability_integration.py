from logging import root

import numpy as np

# alright so integration is actually very important in finance and many other aspects. if we want to find the probability of some action on a bell curve, we dont go around counting how many times we got each. nah too much work. we just find the area under the curve in the required range. or basically finding the definitive integral of the curve in that desired range.
# this gives us the exact probability of that range. and it is very important.

# this function uses the reimann sum method to find the integral of a function between two points. i have set the n_steps to 10000 so it just divides the function's width into 10000 x points
# and we use the array of x points to calculate the y value using the function defined and then just add the y values up times the width. this gives us the integral or the area under the curve between a and b.
def integrate_numerically(func, a, b, n_steps = 10000):
    width = (b-a) / n_steps
    xvalues = np.linspace(a, b, n_steps)
    # print(np.linspace(a, b, n_steps))
    #
    # # so the linspace function basically returns x points equally divided into n_steps through a to b
    # print(type(np.linspace(a, b, n_steps)))

    # so now we know that the np.linspace returns an array. we can just calculate the y values using the function on the x values.


    y_values = func(xvalues)
    # print(y_values)


    return sum(y_values) * width

# testing the above function.

f = lambda x: x**2


f2 = lambda x: np.exp(x)

# testing x^2
print("function x^2")
# print(integrate_numerically(f, 0, 500))
print(integrate_numerically(f, 0, 3))

# testing e^x
print("function e^x")
print(integrate_numerically(f2, 0 , 1))


#####

# just using the function above on normal distribution function to calculate some probabilities.
function = lambda x: (1/(np.sqrt(2*np.pi)))*np.exp((-x**2)/2)
print(integrate_numerically(function, -1, 1))
print(integrate_numerically(function, -10, -2))

