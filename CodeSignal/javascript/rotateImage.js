img = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]



function rotateImage(a) {
    for(var row = 0; row < a.length; row++){
        for(var col = 0; col < row; col++){
            a[row][col], a[col][row] = a[col][row],a[row][col]
        }
    }
    for(var i in a) {
        a[i] = a[i].reverse()
    }
    return a
}

console.log(rotateImage(img))
