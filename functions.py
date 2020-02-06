from math import gcd
def euler_phi(x):
    return None

def mul_order(a, n): #Multiplicative order computation
    if gcd(a, n) != 1:
        print ("Error: the two numbers don't have gcd as 1")
        exit(0)
    k = 1
    while (k >0):
        if((a**k)%n)==1:
            return k
        else:
            k=k+1
