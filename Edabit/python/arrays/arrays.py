list_of_names = ['Sam', 'Bob', 'Trilly']
list_of_names2 = ['Sam', 'Based God', 'Trilly']
list_of_names2 = ['Sam', 'Based God', 'Trilly', 'Bob', 'James']

## My original answer
# def find_bob(names):
# 	for n in names:
# 		if n == 'Bob':
# 			return names.index('Bob')
# 	if 'Bob' not in names:
# 		return -1

## Refactored Solution from Other Folks
def find_bob(names):
	return names.index('Bob') if 'Bob' in names else -1

print(find_bob(list_of_names2))