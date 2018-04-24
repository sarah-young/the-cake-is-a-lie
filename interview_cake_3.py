"""Given a list of integers, find the highest product you can get from three of the integers.

The input list_of_ints will always have at least three integers."""

def highest_product(lst):
    """Find the highest product from a list of three integers"""

    highest = max(lst[0], lst[1]) # seed highest w/ max of 1st two indices
    lowest = min(lst[0], lst[1]) # seed lowest w/ min of 1st two indices

    highest_of_2 = lst[0] * lst[1] # seed highet of 2 w/ 1st two indices
    lowest_of_2 = lst[0] * lst[1] # seed lowest of 2 w/ 1st two indices
    highest_of_3 = lst[0] * lst[1] * lst[2] # seed highest of 3 w/ 1 three indices

    for i in xrange(2, len(lst)): # iterate through list
        current = lst[i] # assign value of list @ i to current
        highest_of_3 = max(highest_of_3,
                           current * highest_of_2,
                           current * lowest_of_2) # re-evaluate highest of 3
        highest_of_2 = max(highest_of_2,
                           current * highest,
                           current * lowest) # re-evaluate highest of 2
        lowest_of_2 = min(lowest_of_2,
                          current * highest,
                          current * lowest) # re-evaluate lowest of 2
        highest = max(highest, current) # re-evaluate highest
        lowest = min(lowest, current) # re-evaluate lowest

    # by looping through the list and multiplying all the variables by lowest
    # and highest allows for negative numbers and double negatives to be taken
    # into account    

    return highest_of_3

lst = [1, 10, -5, 1, -100]

hp = highest_product(lst)

print hp
