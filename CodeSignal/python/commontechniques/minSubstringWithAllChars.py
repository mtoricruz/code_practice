# Understanding
# 

# Planning
#

# Execute

# Refactor/Reflection
def minSubstringWithAllChars(s, t):
    if not t: return ''
    if t == s: return t
    L = len(t)
    t = set(t)

    while L < len(s):
        for i in range(0, len(s) - L+1):
            subs = set(s[i:i+L])
            if subs.issuperset(t):
                return s[i:i+L]
        L += 1