from functions import mul_order
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
    r = 2
    while r > 0:
        if mul_order(r, number)>16:
            return r
        else:
            r = r+1

def test(number):
    return mul_order(number, 7)

if __name__ == "__main__":
    #num_input = int(input("Please input an positive integer: "))
    #print (primes(3434351))
    #print (primes_sieve(num_input))
    print (test(8))