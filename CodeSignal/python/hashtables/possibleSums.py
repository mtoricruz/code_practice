# Understanding
# 2 lists as arguments
# coins list of coin value and quantity list of amount of coins
# how many DISTINCT sums wrap final return in set() 
# single coin value = sum
# no restriction on space complexity - create a results set(list)
# notice that list of len(coins) * len(quantity) = correct possible sums
# create hashtable where keys would be possible sums
# can loop through both lists at the same time using zip()
    # for coin, amount in zip(coins, quantity)

# Planning
# d = {}
# results = []
# for each value in coins:
    # if value not in d:
        # d[value] = 1
    # else:
        # for each amount in quantity:
            # possibleSum = value * amount
        # if possibleSum not in d:
            # d[possibleSum] = 1
# results.append(d.keys())
# return len(set(results))

# Execution my attempt
def possibleSums(coins, quantity):
    d = {}
    sums = []
    for idx, coin in enumerate(coins):
        idxSum = coin * quantity[idx]
        sums.append(idxSum)
    total = sum(sums)
    return total

# Reflection/Refactor
def possibleSums(coins, quantity):
    # initialize possible_sums set to 0
    possible_sums = {0}
    # loop thru each coin/amount together using zip()
    for coin, amount in zip(coins, quantity):
        # for each sum in possible_sums frozen: (frozenset() to keep original sums before adding new amounts to set during current iteration)
        for s in frozenset(possible_sums):
            # for each amount of coins in range(1, amt + 1)
            for amount in range(1, amount + 1):
                # add possible sum
                possible_sums.add(coin * amount + s)
    # return len(possible_sums) - 1
    return len(possible_sums) - 1