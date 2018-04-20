"""You have a list of integers, and for each index you want to find the product of every integer except the integer at that index.

Write a function get_products_of_all_ints_except_at_index() that takes a list of integers and returns a list of the products.

For example, given:

  [1, 7, 3, 4]

your function would return:

  [84, 12, 28, 21]

by calculating:

  [7 * 3 * 4,  1 * 3 * 4,  1 * 7 * 4,  1 * 7 * 3]

Do not use division in your solution."""

def get_products_of_all_ints_except_at_index(lst):
    """Take a list of ints and return product of ints not including the value of the current index"""
    new_lst = []

    for i in range(len(lst)):

        for j in range(len(lst)):
            product = 1
            if j != i:
                product = product * lst[j]
        new_lst.append(product)

    return new_lst

lst = [1, 7, 3, 4]
sum_lst = get_products_of_all_ints_except_at_index(lst)
print sum_lst