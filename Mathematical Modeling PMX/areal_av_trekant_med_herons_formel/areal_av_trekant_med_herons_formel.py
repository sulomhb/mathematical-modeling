import numpy as np   
def areal(a,b,c):
    s = (1/2)*(a+b+c)
    return np.sqrt(abs(s*(s-a)*(s-b)*(s-c))) 

a = float(input("a = :"))
b = float(input("b = :"))
c = float(input("c = :"))

while True:
    try:
        print(areal(a,b,c))
    except:
        print("Skriv inn tall høyere enn 0")