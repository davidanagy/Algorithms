#!/usr/bin/python

import sys


# I confess I don't *fully* grok how the following code works, but after
# adding the print statements (now commented out) and thinking about it,
# I believe it's something like this:
# Start by defining cache[0] as 1.
# Now, you run through a for-loop with each coin. The result of the for-loop is
# computing how many ways there are to make change with **just** the coin
# **and** the previous coins you've already done this for. So when we run
# through with pennies first, we just end up with 1's because there's only
# one way to make change with only pennies.
# Now add nickels. We start at 5 cents (since nickels obviously aren't)
# applicable to any amount below 5). For each higher_amount,
# we want to know how many ways there are to make change *once* you use
# the single nickel. So for instance, 5-5 is 0, and cache[0] is 1. This means
# that adding the nickels gives you one **additional** way to make change for
# 5 cents, so you add one to cache[5]. Same for 6 through 9.
# What happens when you arrive at 10? 10-5 is 5, so you ask how many ways
# there are to make change with 5 cents (with only pennies and nickels).
# But we already know this from earlier in the loop--just get cache[5],
# which is 2! So adding nickels gives you **two** additional ways to get
# change for 10 cents, and you add 2 to cache[10]. Repeat this process
# for all higher_amounts and all coins, and you get your answer.
def making_change(amount, denominations):
    # Initialize cache
    cache = [0] * (amount+1)
    # Set base cache: there's one way to make change for zero cents
    cache[0] = 1
    for coin in denominations:
        #print('Start:', coin, cache)
        # loop through all higher amounts between the coin and the amount
        for higher_amount in range(coin, amount+1):
            # use our cache to find out how many ways there are to make
            # the higher amount after subtracting the given coin
            difference = higher_amount - coin
            ways = cache[difference]
            # add this to the relevant index in the cache
            cache[higher_amount] += ways
        #print('End:', coin, cache)

    return cache[amount]


if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")