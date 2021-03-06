import math

import warnings

def isPrime(num):
    """
    Checks if the number is prime

    Parameters
    ----------
    num : int
        denotes a natural number 
    return : bool
        return true if the number is prime otherwise returns false

    """
    if(num < 0):
        raise ValueError(
            "num must be a natural natural"
        )

    if(num <= 1):
        return False
    if(num <= 3):
        return True
    if(num%2 == 0 or num%3==0):
        return False

    i = 5

    while(i*i <= num):
        if(num%i == 0 or num%(i+2) == 0 ):
            return False
        i = i + 6

    return True

def prime_series(count):
    """
    Returns an array of prime numbers

    Parameters
    ----------
    count : int
        denotes the count of prime numbers
    return : array
        return an array of length 'count'

    """
    if(count < 0 or int(count)!=count):
        raise ValueError(
            "Input must be a non-negative integer"
        )

    arr_prime = []
    i=0
    j=2

    while(i!=count):
        if(isPrime(j)):
            arr_prime.append(j)
            j = j + 1
            i = i + 1
        else:
            j = j + 1

    return arr_prime

def prime(n):
    """
    Returns n'th prime number

    Parameters
    ----------
    n : int
        denotes the position of prime number
    return : int
        returns an integer
    """
    return (prime_series(n))[-1]
    
def prime_table(count):
    """
    Returns an array of numbers of prime-table

    Parameters
    ----------
    count : int
        denotes a non-negative integer
    return : array
        returns an array of length 'count'

    """
    if(count < 0 or int(count)!=count):
        raise ValueError(
            "count must be a non-negative integer"
        )

    prime_array = prime_series(count)

    for i in range(1,len(prime_array)):
        prime_array[i] = prime_array[i] * prime_array[i-1]

    prime_table_array = [i+1 for i in prime_array]

    return prime_table_array

def SieveOfEratosthenes(*args):
    """
    Returns prime numbers within a range (including lower and upper bounds) or prime numbers less than or equal to given input

    Parameters
    ----------
    *args : tuple
        Expects one or two arguments as described below

    Other Parameters
    ----------------
    1 argument : int
        denotes upper bound for prime numbers
    2 arguments : (int,int)
        denotes lower and upper bounds for range of prime numbers
    
    Returns
    -------
    array
        returns an array of prime numbers

    """
    if(len(args)==1):
        n = args[0]
        prime = [True for i in range(n+1)]
        p = 2
        while (p * p <= n):
            if (prime[p] == True):
                for i in range(p * p, n+1, p):
                    prime[i] = False
            p += 1
        prime_arr = []    
        for p in range(2, n+1):
            if prime[p]:
                prime_arr.append(p)
        return prime_arr
    elif(len(args)==2):
        low = args[0]
        high = args[1]
        n = args[1]
        prime = [True for i in range(n+1)]
        p = 2
        while (p * p <= n):
            if (prime[p] == True):
                for i in range(p * p, n+1, p):
                    prime[i] = False
            p += 1
        prime_arr = []    
        for p in range(2, n+1):
            if (prime[p] and p>=low):
                prime_arr.append(p)
        return prime_arr
    elif(len(args)>2):
        raise NotImplementedError(
            "Invalid Number Of Arguments"
        )

#def prime_divisors
#def prime_factorizatio
