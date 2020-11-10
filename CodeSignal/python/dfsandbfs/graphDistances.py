# Understanding

# Planning

# Execute

# Refactor/Reflection
def graphDistances(g, s):
    length = len(g)
    for i in range(length):
        g[i][i] = 0
    
    arr = g[s]
    ls = set(range(length))
    ls.remove.(s)

    while ls:
        pos = -1
        mini = float('inf')
        for each in ls:
            if(arr[each] < mini and arr[each] != -1):
                pos = each
                mini = arr[each]
        
        ls.remove(pos)
        for each in ls:
            if(g[pos][each] != -1):
                if(arr[each] == -1):
                    arr[each] = arr[pos] + g[pos][each]
                else:
                    arr[each] = min(arr[each], arr[pos] + g[pos][each])

    return arr