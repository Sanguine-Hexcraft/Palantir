import math
import decimal

def calculate_pi(precision):
    '''Calculates pi to a specified number of decimal places using the Chudnovsky algorithm.'''
    decimal.getcontext().prec = precision + 1
    C = 426880 * decimal.Decimal(math.sqrt(10005))
    L = decimal.Decimal(13591409)
    X = decimal.Decimal(1)
    K = decimal.Decimal(6)
    sum_terms = decimal.Decimal(L)  # Initialize with the first L value
    for i in range(1, precision + 1):
        L = decimal.Decimal(545140134) + L
        X = X * (-262537412640768000)
        K = K + 12
        T = (decimal.Decimal(K) * L) / X
        sum_terms += T
    pi = C / sum_terms
    return str(pi)[:precision+1]


if __name__ == '__main__':
    precision = 100  # You can change this to the desired number of digits
    pi_value = calculate_pi(precision)
    print(f"Pi to {precision} digits: {pi_value}")