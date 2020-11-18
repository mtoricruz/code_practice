def commonCharacterCount(s1, s2):
    list1 = list(s1)
    list2 = list(s2)
    count = 0
    for char in list1:
        if char in list2:
            count += 1
            list2.remove(char)
    return count