

"""
Context:
april 15 11:41 pm. Taylor Series and ODES.
So I did taylor series and odes tonight. sin(x) and e^x expansions make sense visually now. it was pretty hard to imagine at first. but the actual hard part was the differential equations classifying by order and degree and then solving them. variable separable method is alright but the substitution ones was a bit messy but i got it pretty quick.
also worked through the dy/dx = (x+y-1)/(x+y+1) example by hand. taking x+y+1=t makes the integration way easier but keeping track of the dt/dx substitution got me confused for a bit.
made a taylor series from scratch with a changing sign loop instead of just using a math library and i also built like an euler solver
feeling good because its sleep time now. HAHA
"""


import numpy as np
import math

def taylor_approx_sin(x, terms):

    is_positive = bool(True)
    total_val = 0
    for i in range(1, terms + 1):

        base_structure = (x**((2*i)-1))/(math.factorial(2*i - (1)))

        if is_positive:
            is_positive = False
        else:
            base_structure = -(base_structure)
            is_positive = True

        print(base_structure)

        total_val += base_structure

    return total_val


def euler_ode_solver(y0, r, t, steps):
    dt = t / steps

    y = y0

    for i in range(steps):
        y = y + (r*y) * dt

    return y



print(taylor_approx_sin(np.pi/2, 5))

print(euler_ode_solver(100, 0.05, 2, 1000))

