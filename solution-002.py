"""
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

//4613732
"""


n1,n2=2,3
toplam=0

while(n1< 4000000):
    if(n1%2 == 0):

        toplam = n1 + toplam

        t=n1 #t=takas
        n1 = n2
        n2 = t + n2
    else:
        t = n1
        n1 = n2
        n2 = t + n2

print(toplam)
