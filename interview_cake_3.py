"""Given a list of integers, find the highest product you can get from three of the integers.

The input list_of_ints will always have at least three integers."""

def highest_product(lst):
    """Find the highest product from a list of three integers"""

    highest = max(lst[0], lst[1])
    lower = min(lst[0], lst[1])

    highest_of_2 = lst[0] * lst[1]
    lowest_of_2 = lst[0] * lst[1]
    highest_of_3 = lst[0] * lst[1] * lst[2]

    for i in xrange(len(lst) - 2)
    # set variable "current" to lst[i]
    # use min and max functions to find new highest and lowest products for each variable
    # once loop is completed, return highest of three amount



lst = [1, 10, -5, 1, -100]

hp = highest_product(lst)

print hp
