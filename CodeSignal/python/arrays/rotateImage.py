# Note: Try to solve this task in-place (with O(1) additional memory), since this is what you'll be asked to do during an interview.

# You are given an n x n 2D matrix that represents an image. Rotate the image by 90 degrees (clockwise).

# For

img = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
     

# rotateImage(a) =
#     [[7, 4, 1],
#      [8, 5, 2],
#      [9, 6, 3]]

# U 
# 2d array of images
# rotate clockwise, 90deg
# reverse arr
# transpose the matrix
# transposing is fliping a matrix over it's diagonal
# take the reversed arr
# [[7, 8, 9], 
#  [4, 5, 6], 
#  [1, 2, 3]]
# transposing the arr results in
#  [[7, 4, 1],
#      /  /
#   [8, 5, 2],
#      /  /
#   [9, 6, 3]]
# swapping 4,8 / 1, 9 / 2, 6

# E
def rotateImage(a):
    a.reverse()
    for row in range(len(a)):
        for col in range(row):
            a[i][j], a[j][i] = a[j][i], a[i][j]
    return a

# R
print(rotateImage(img))
# http://www.pythontutor.com/visualize.html#code=img%20%3D%20%5B%5B1,%202,%203%5D,%0A%20%20%20%20%20%5B4,%205,%206%5D,%0A%20%20%20%20%20%5B7,%208,%209%5D%5D%0A%0Adef%20rotateImage%28a%29%3A%0A%20%20%20%20a.reverse%28%29%0A%20%20%20%20for%20i%20in%20range%28len%28a%29%29%3A%0A%20%20%20%20%20%20%20%20for%20j%20in%20range%28i%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20a%5Bi%5D%5Bj%5D,%20a%5Bj%5D%5Bi%5D%20%3D%20a%5Bj%5D%5Bi%5D,%20a%5Bi%5D%5Bj%5D%0A%20%20%20%20return%20a%0A%0Aprint%28rotateImage%28img%29%29&cumulative=false&curInstr=22&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false