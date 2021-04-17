from fractions import Fraction
from functools import reduce

def product(fracs):
    multi=1
    for i in fracs:
        multi=multi*i 
    return multi.numerator, multi.denominator
    # return t.numerator, t.denominator

if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)