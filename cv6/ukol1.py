from cmath import sqrt
import numpy as np
from math import sqrt

def is_prime(n):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(n**0.5)
  f = 5
  while f <= r:
    if n % f == 0: return False
    if n % (f+2) == 0: return False
    f += 6
  return True    

def find_nth_prime(nth):
    count = 0
    num = 1
    run = True
    while(run == True):
        if is_prime(num) == True:
            count += 1
            print("{0}nth prime is: {1}".format(count, num))

        num += 1

        if count == nth:
            run = False
    print("LADIES AND GENTLEMAN, WE GOT THEM: ", num-1)
        


find_nth_prime(1000000)

    