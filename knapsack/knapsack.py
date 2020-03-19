#!/usr/bin/python

import sys
from collections import namedtuple

Item = namedtuple('Item', ['index', 'size', 'value'])


# The function below works correctly. But it can take a while.
# It took approximately 20 seconds for each "medium" file (200 rows),
# and around 980 seconds (16 minutes) for the "large" file (1000 rows)
# on my computer. But I'm not sure if/how I can get it to run faster.
# I made an optional "fast" parameter to use the function below it instead,
# which is much faster but occasionally slightly inaccurate.
def knapsack_solver(items, capacity, fast=False):
    if fast:
        return knapsack_solver_fast(items, capacity)

    # create cache
    cache = {}
   
    def fill_item_bag(item_bag, items, capacity, total_value):
        """Takes a list of items in your bag, a list of remaining items,
        the remaining capacity of your bag, and the total value of your bag.
        Returns a list of items that, if picked up, maximizes the value of
        your bag, as well as the new total value of the bag."""
        num_items = len(items)
        if num_items == 0:
            # If no remaining items, just return the current bag
            # since we've picked everything up.
            return item_bag, total_value

        if total_value in cache.keys():
            items_column = cache[total_value]
            if capacity in items_column.keys():
                # If the relevant total_value/capacity pair exists in the
                # cache, return it.
                # (The print statement was used to make sure the cache
                # was being used correctly; it was, I think.)
                #print('cache used')
                return items_column[capacity]
        else:
            # Otherwise, create a new sub-dictionary in the cache.
            cache[total_value] = {}
            items_column = cache[total_value]

        # Default values for max_value and max_value_bag
        max_value = total_value
        max_value_bag = item_bag
        for item in items:
            # Only pick up an item if its size is smaller or equal
            # to the remaining capacity
            if item.size <= capacity:
                # Create copies so we don't mess with the original lists
                new_item_bag = item_bag.copy()
                new_items = items.copy()
                # Add the item to the bag and remove it from "items"
                new_item_bag.append(item)
                new_items.remove(item)
                # Calculate a new remaining capacity and total value
                new_capacity = capacity - item.size
                new_total_value = total_value + item.value
                # Recursion
                filled_bag, filled_bag_value = fill_item_bag(new_item_bag, new_items,
                                                new_capacity, new_total_value)
                # If this results in more value than the previous attempts,
                # log the new total value and bag as max_value and max_value_bag
                if filled_bag_value > max_value:
                    max_value = filled_bag_value
                    max_value_bag = filled_bag
        
        # Update the cache so it includes the current total_value and capacity
        items_column[capacity] = (max_value_bag, max_value)
        # Return BOTH the bag AND its value. This saves much computing time,
        # so that we don't have to sum up the values in the bag each time.
        return max_value_bag, max_value

    # Run the above function
    max_value_bag, value = fill_item_bag([], items, capacity, 0)
    # Get the index numbers of the bag, and sort them so they're in order
    index_nums = sorted([item.index for item in max_value_bag])
    # Put the results in the specified format
    return_dict = {'Value': value, 'Chosen': index_nums}
    return return_dict


# The function below runs very fast, but it sometimes leads to false results
# for odd datasets. For isntance, it works for all the "small" and "medium"
# text files, but not the "large" one. The reason is items 329, 700, and 987:

# Index Size Value True_Value (Value/Size)
# 329    1    15             15
# 700    1    11             11
# 987    2    27             13.5

# The algorithm below picks items up in order ot True_Value, as long as they don't
# put us above capacity. When it reaches item 329, our total weight is 98,
# so it can pick up 329. But at that point we're at weight 99, so we can't
# # pick up 987 or we'll go above capacity. As such, it just picks up 700
# and ends. In other words, because it **only** picks up items in order of
# True_Value and can't "look ahead", it ends up with one lower total value than
# it should, since 987 by itself is worth more than 329 and 700.
# I can't think of a way to solve this problem without just turning it into
# the second function below, so I decided to just turn it into a "fast" version
# that you can use via parameter in the main one.
def knapsack_solver_fast(items, capacity):
    # Make a new namedtuple, with a "true_value" attribute
    ItemNew = namedtuple('ItemNew', ['index', 'size', 'value', 'true_value'])
    new_items = []
    for item in items:
        # "true_value" is just the item's value divided by its size
        true_value = item.value / item.size
        new_item = ItemNew(item.index, item.size, item.value, true_value)
        new_items.append(new_item)

    # helper function for the sort method below
    def sort_by_true_value(item):
        return item.true_value

    # Sort the new items by their true_value (hence the "key" argument),
    # largest to smallest.
    new_items.sort(key=sort_by_true_value, reverse=True)
    # Start with an empty bag and 0 weight
    item_bag = []
    weight = 0
    # Iterate through the new_items in order
    for item in new_items:
        # Only pick up an item if it doesn't take us above capacity
        if weight + item.size <= capacity:
            # Pick up the item
            item_bag.append(item)
            # Add its size to our current weight
            weight += item.size

    # Get the total value of our items
    value = sum([item.value for item in item_bag])
    # Get index numbers of our items, in order
    index_nums = sorted([item.index for item in item_bag])
    # Put results into proper format
    return_dict = {'Value': value, 'Chosen': index_nums}
    return return_dict
  

if __name__ == '__main__':
  if len(sys.argv) > 1:
    capacity = int(sys.argv[2])
    file_location = sys.argv[1].strip()
    file_contents = open(file_location, 'r')
    items = []

    for line in file_contents.readlines():
      data = line.rstrip().split()
      items.append(Item(int(data[0]), int(data[1]), int(data[2])))
    
    file_contents.close()
    fast = False
    if len(sys.argv) > 3:
      if sys.argv[3].lower() == 'fast':
        fast = True
    print(knapsack_solver(items, capacity, fast))
  else:
    print('Usage: knapsack.py [filename] [capacity] [optional: "fast" for faster but less accurate results]')