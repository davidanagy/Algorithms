#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, cache=None):
    if cache is None:
        cache = [0] * (n+1)
    if cache[n] != 0:
        return cache[n]

    num_ways = 0
    # Can he eat three cookies?
    if n >= 3:
        # Eat three cookies.
        # Save as separate variable so "n" is preserved
        # for the following if statements.
        k = n-3
        #print('Ate three cookies.')
        # See how many ways there are to eat the remaining cookies.
        # This gives us how many ways he can eat the cookies if he
        # starts by eating 3, so increment that to num_ways.
        num_ways += eating_cookies(k, cache)
        #print(f'Cookies: {k}; num_ways: {num_ways}')
    # Repeat the above with 2 and 1.
    # Make them "if" and not "elif" because we want to cover
    # all of the conditionals.
    if n >= 2:
        k = n-2
        #print('Ate two cookies.')
        num_ways += eating_cookies(k, cache)
        #print(f'Cookies: {k}; num_ways: {num_ways}')
    if n >= 1:
        k = n-1
        #print('Ate one cookie.')
        num_ways += eating_cookies(k, cache)
        #print(f'Cookies: {k}; num_ways: {num_ways}')
    elif n == 0:
        #print('Ate no cookies.')
        num_ways += 1
    else:
        pass

    cache[n] = num_ways
    return num_ways

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')