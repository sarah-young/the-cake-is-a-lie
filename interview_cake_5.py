"""Your quirky boss collects rare, old coins...

They found out you're a programmer and asked you to solve something they've been wondering for a long time.

Write a function that, given:

an amount of money
a list of coin denominations
computes the number of ways to make the amount of money with coins of the available denominations.

Example: for amount=4 (4¢) and denominations=[1,2,3][1,2,3]
(11¢, 22¢ and 33¢), your program would output 4—the number of ways to make 4¢
with those denominations:

1¢, 1¢, 1¢, 1¢
1¢, 1¢, 2¢
1¢, 3¢
2¢, 2¢

"""

def coins(amount, denominations)

    answer = 0

    for denomination in denominations:
        for each num_times_to_use_denomination in \
                possible_num_times_to_use_denomination_without_overshooting_amount:
            answer += number_of_ways(amount_remaining, other_denominations)
    return answer
