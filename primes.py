from functions import mul_order
from math import log2
#The algorithm used here is "Sieve of Eratosthenes"
#See https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

def primes_sieve(number):
    isprime = (number+1)*[True]
    for n in range (2,number+1):
        if isprime[n] == True:
            for i in range(2*n, number+1, n):
                isprime[i]= False
    return isprime[-1]

def primes_aks(number):
    #The AKS Primality test is a deterministic primality-proving algotithm.
    #AKS is the first primality-proving algorithm to be simultaneously general, polynomial, deterministic, and unconditional.
    #See https://en.wikipedia.org/wiki/AKS_primality_test
    
    if number <=1 :
        print("Integer input needs to be greater than 1")
        exit(0)
    for a in range(1, number+1):
        for b in range(2, int(log2(number))+1):
            if number == a**b:
                print ("number is composite")
                exit(0)
    


def test(number):
    return mul_order(number, 7)

if __name__ == "__main__":
    #num_input = int(input("Please input an positive integer: "))
    #print (primes(3434351))
    #print (primes_sieve(num_input))
    #print (test(8))
    print (primes_aks(16))