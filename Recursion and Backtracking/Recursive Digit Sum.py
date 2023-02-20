#We define super digit of an integer  using the following rules:

#Given an integer, we need to find the super digit of the integer.

#If  has only  digit, then its super digit is .
#Otherwise, the super digit of  is equal to the super digit of the sum of the digits of .
#For example, the super digit of 

def sup_digits(x,k):
    a = digsum(x)
    return sup_digit(str(int(a)*k))

def sup_digit(x):
    if len(x) <= 1:
        return x
    else:
        return sup_digit( digsum(x) )

def digsum(x):
    return str(sum((int(i) for i in list(x))))


n, k = input().split()
print( sup_digits(n, int(k)))