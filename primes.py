
#The algorithm used here is "Sieve of Eratosthenes"
#See https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

def primes(number):
    isprime = (number+1)*[True]
    for n in range (2,number+1):
        if isprime[n] == True:
            for i in range(2*n, number+1, n):
                isprime[i]= False
    return isprime[-1]

num_input = int(input("Please input an positive integer: "))
#print (primes(3434351))
print (primes(num_input))