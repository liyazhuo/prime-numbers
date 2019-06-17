from math import gcd
def euler_phi(x):
    return None

def mul_order(a, n): #Multiplicative order computation
    k = 1
    while (k >0):
        if(n**k)%(a)==1:
            return k
        else:
            k=k+1
