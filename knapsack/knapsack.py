#!/usr/bin/python

import sys
from collections import namedtuple

Item = namedtuple('Item', ['index', 'size', 'value'])

def knapsack_solver(items, capacity):
   
    def fill_item_bag(item_bag, items, capacity):
        if len(items) == 0:
            return item_bag

        if len(item_bag) == 0:
            total_size = 0
            max_value = 0
        else:
            total_size = sum([item.size for item in item_bag])
            max_value = sum([item.value for item in item_bag])
        max_value_bag = item_bag
        for item in items:
            if (total_size + item.size) < capacity:
                new_item_bag = item_bag.copy()
                new_items = items.copy()
                new_item_bag.append(item)
                new_items.remove(item)
                filled_bag = fill_item_bag(new_item_bag, new_items, capacity)
                total_value = sum([item.value for item in filled_bag])
                if total_value > max_value:
                    max_value = total_value
                    max_value_bag = filled_bag
        return max_value_bag

    max_value_bag = fill_item_bag([], items, capacity)
    value = sum([item.value for item in max_value_bag])
    index_nums = [item.index for item in max_value_bag]
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
    print(knapsack_solver(items, capacity))
  else:
    print('Usage: knapsack.py [filename] [capacity]')