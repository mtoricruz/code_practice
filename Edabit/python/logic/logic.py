# Learning from edabit's minimal series, where we replace regular functions with lambda functions
# must replace:
# def add_x(x):
#   return x + x
# with
# add_x = lambda x: x + x

# def add_2(x):
# 	return x + 2
add_2 = lambda x: x + 2

add_3 = lambda x: x + 3

add_5 = lambda x: x + 5

add_7 = lambda x: x + 7

add_11 = lambda x: x + 11


print(add_2(3)) 
print(add_3(3))
print(add_5(3))
print(add_7(3))
print(add_11(3))
# 5
# 6
# 8
# 10
# 14

# Other solutions:
# From Haksell (13,985 xp which is 2,797 challenges completed without spoilers)
# for n in range(12):exec("add_%s=lambda x:x+%s"%(n,n))