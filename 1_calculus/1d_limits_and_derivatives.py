import numpy as np

def numerical_limit(func, x, h=1e-7):
    numerator = func(x+h) - func(x)
    denominator = h
    return numerator / denominator


# testing a basic function f(x) = x^2 to see if the numerical limit function even works.
f = lambda x: x**2

result = numerical_limit(f, 3)

print(f"the derivative of x^2 when x = 3 is: {result}")

# also the output is really close to 6. (its 6.000000087880153, which is fine)



# now proving the power rule i.e., f(x) = x^n . then f'(x) = n * x^n-1

# I will try to do a manual power rule derivative calculation along with the function numerical_limit. they should be close if not the same.

f2 = lambda x: x**5
function_result = numerical_limit(f2, 2)
manual = 5 * (2 ** 4)

print(np.isclose(function_result, manual))

#Boom. they are close. as the output is true. Yes

def log_return_derivative(P_t, P_t_minus1):

    # the original function. wrote it to give me some context and not get distracted. but its useless here since it wont be used.
    # log_return = ln(P_t) - ln(P_t_minus1)

    # deriving ln(price_today) is very easy to do manually as well. derivative of any ln(x) is just (derivative of x)/x

    log_der = (1/P_t) - 0
    return log_der

    # negative 0 because ln(price_yesterday) is a constant and derivative of a constant is always 0
    # yesterday's price doesnt change at all no matter how much today's price fluctuates.




# testing the function above.

print(log_return_derivative(101, 100))
print(log_return_derivative(10, 9))

