#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
    # Define default total_batches
    total_batches = None
    # Iterate through each key in the "recipe" dictionary
    for key in recipe.keys():
        # Our goal is to find the **minimum** number of batches we
        # can make of each ingredient, since if we don't have
        # enough of even one ingredient we can't make the recipe.
        if key not in ingredients.keys():
            # If the key isn't in the "ingredients" dictionary,
            # that means we don't have any of that ingredient,
            # so we can make 0 batches.
            # Zero is the lowest number of batches we can have,
            # so might as well end the loop here.
            total_batches = 0
            break
        else:
            # Otherwise, do floor division to find batches.
            batches = ingredients[key] // recipe[key]
            if batches == 0:
                # Zero is the lowest number of batches we can have,
                # so might as well end the loop here.
                total_batches = 0
                break
        if total_batches is None:
            # If "total_batches" is None, that means this is the first
            # key, so just define total_batches as "batches".
            total_batches = batches
        else:
            if batches < total_batches:
                # Again, we're looking for the **minimum** number of
                # batches. So replace total_batches with batches
                # if "batches" is smaller.
                total_batches = batches

    return total_batches


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))