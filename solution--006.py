"""
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

//25164150
"""


karetoplam=0
toplam=0
for i in range(101):
    karetoplam=karetoplam+(i*i)
    toplam=toplam+i

if(karetoplam>(toplam*toplam)):
    print(karetoplam-(toplam*toplam))
else:
   print((toplam * toplam)-karetoplam)