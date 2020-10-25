dishes = [["Salad", "Tomato", "Cucumber", "Salad", "Sauce"],
     ["Pizza", "Tomato", "Sausage", "Sauce", "Dough"],
     ["Quesadilla", "Chicken", "Cheese", "Sauce"],
     ["Sandwich", "Salad", "Bread", "Tomato", "Cheese"]]

# Understanding
# 2d array
# starts out grouped by name of the dish>its ingredients
# group dishes by ingredients>names of dish with ingredient
# names of dishes to be sorted lexicographically
# list dish with ingredient if there's at least 2 such dishes (>= 2)
# return array where each element is a list beginning with ingredient

# loop through final element list, split->sort->join

# Planning
# initialize empty dict + results arr
# loop thru dishes array 
    # access ingredients by looping thru all of elements to the right of the 1st index
        # if ingredient is not in dict, initialize empty list to store dishes in
    # for every ingredient.append(elem[0]), then sort()
# loop thru food dict.items():
    # insert(0, ingredient)
    # if len(ingredient & dishes) >= 3:
        # append(v) to results
# results.sort()
# return results


# Execution
# def groupingDishes(dishes):
#     food = {}
#     results = []
#     # loop through each element in dishes array
#     for elem in dishes:
#         for ingredient in elem[1:]:
#             if ingredient not in food:
#                 food[ingredient] = []
#             food[ingredient].append(elem[0])
#             food[ingredient].sort()
#     for k, v in food.items():
#         v.insert(0, k)
#         if len(v) >= 3:
#             results.append(v)
#     results.sort()
#     return results

# Reflect/Refactor
def groupingDishes(dishes):
    D = {}
    for dish in dishes:
        dish_name = dish.pop(0)
        for ingred in dish:
            D[ingred] = D.get(ingred, []) + [dish_name]
    return sorted([i] + sorted(v) for i, v in D.items() if len(v) > 1)
print(groupingDishes(dishes))