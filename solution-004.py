"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

//906609
"""

list=[]
for n1 in range(100,999):
    for n2 in range(100, 999):
        x=n1*n2
        s=str(x)
        t=s[::-1]
        if s==t:  #polidrom sayi
            list.append(int(s))
print(max(list))

