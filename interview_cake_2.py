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

    products_of_all_ints_before_index = [None] * len(lst)

    product = 1

    for i in xrange(len(lst)):
        products_of_all_ints_before_index[i] = product
        # assigning current product to index of new get_products_of_all_ints_except_at_index
        # this takes '1' first so it's always one step behind
        product *=lst[i]
        # multiplying the product by the index so on the next round it will be added as the next index in the new get_products_of_all_ints_except_at_index
        print "Product: ", product

    product = 1
    for i in xrange(len(lst)-1, -1, -1):
        products_of_all_ints_before_index[i] *= product
        # multiplying by the product of everything after the index
        # starting @ lst[-1]
        product *= lst[i]
        print "Product: ", product

    return products_of_all_ints_before_index


# FIRST ATTEMPT, CORRECT ANSWER, POOR RUNTIME
    # new_lst = []
    #
    # for i in xrange(len(lst)):
    #
    #     product = 1
    #     for j in xrange(len(lst)):
    #         if j != i:
    #             product = product * lst[j]
    #     new_lst.append(product)
    #
    # return new_lst

lst = [1, 7, 3, 4]
sum_lst = get_products_of_all_ints_except_at_index(lst)
print sum_lst
