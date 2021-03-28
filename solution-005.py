"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

//232792560
"""


"""
import sys
x=150000
sys.setrecursionlimit(x)

def fonk(s):

    for i in range(1,21):
        if(s%i!=0):
            return fonk(s+1)
    return s

print(fonk(232790000))
"""
import fractions

s=1
for i in range(1, 21):
    s *= i // fractions.gcd(i, s)
print(s)