"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

//104743



#########
sayi=1
count=0
while(count!=10001):
    if sayi > 1:

        for i in range(2, sayi):
            if (sayi % i) == 0:
                sayi+=1
                break

        else:

            count+=1
            if(count==10001):
                print(sayi)
            else:
                sayi += 1

    else:
        sayi+=1

"""
sayi=1
list=[]
while(len(list)<10001):
    if sayi > 1:
        for i in range(2, sayi):
            if (sayi % i) == 0:
                sayi+=1
                break

        else:
            list.append(sayi)
            sayi+=1

    else:
        sayi+=1

print(max(list))