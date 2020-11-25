# Understanding
# \n marks new subdirectory
# find longest path to a file (NOT empty subdirecty)
# files are marked with "." within name 
# some suffix of .png/.txt/etc.
# traversal through string to find "."
# if no "." that means no files, so return 0 

# Planning
# if not fileSystem:
    # return 0

# while fileSystem:
    # 

# Execute

# Refactor/Reflection
# docs on .splitlines(): https://www.programiz.com/python-programming/methods/string/splitlines
def longestPath(fileSystem):
    maxlen = 0
    pathlen = {0:0}
    for line in fileSystem.splitlines():
        name = line.lstrip('\t')
        depth = len(line)-len(name)
        if '.' in name:
            maxlen = max(maxlen, pathlen[depth]+len(name))
        else:
            pathlen[depth+1] = pathlen[depth] + len(name) + 1
    return maxlen