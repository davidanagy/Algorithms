#!/usr/bin/python

import argparse

def find_max_profit(prices):
    # Define default values for min_price_so_far and
    # max_profit_so_far
    min_price_so_far = prices[0]
    max_profit_so_far = prices[1] - prices[0]
    for price in prices[1:]:
        # Since we're subtracting each price by an *earlier* price,
        # we start with the second price
        profit = price - min_price_so_far
        if price < min_price_so_far:
            # Replace min_price_so_far with the smaller price.
            # It's important to do this check *after* defining
            # profit, or else we might end up subtracting
            # the price by itself (if min_price_so_far becomes price).
            min_price_so_far = price
        if profit > max_profit_so_far:
            # Replace max_profit_so_far with the bigger profit.
            max_profit_so_far = profit

    return max_profit_so_far


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))