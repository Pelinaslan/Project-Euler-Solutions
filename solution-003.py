"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

//6857
"""
i = 2
sayi=600851475143
carpan = []
asalcarpan=[]

while (i < (sayi)):
    if (((sayi) % i) == 0): #sayinin carpani
        print(i)
        carpan.append(i)
    i += 1



for s in carpan:
    if(s>1):
        for i in range(2,s):
            if((s%i)==0):
                break
        else:
            asalcarpan.append(s)

print(asalcarpan[len(asalcarpan)-1])


