// Given an array a that contains only numbers in the range from 1 to a.length, 
// find the first duplicate number for which the second occurrence has the minimal index. 
// In other words, if there are more than 1 duplicated numbers, 
// return the number for which the second occurrence has a smaller index than the second occurrence of the other number does. 
// If there are no such elements, return -1.

a = [2, 1, 1, 3, 5, 3, 2]

// U
// Find the FIRST dupe number in array
// the first duplicate at the earliest index, not all dupes
// return index value of first dupe
// if there are no dupes, return -1

// P
// initialize empty arr
// loop through arr
//   

// E
function firstDuplicate(arr) {
    let results = []
    for(i of arr){
        if(results[i])
            return i
        results[i] = 1;
    }
    return -1
}

console.log(firstDuplicate(a))

// R
// One thing that could've helped me solve this faster 
// is to push out more print statements of what i'm doing
// Quickly verify what i'm trying to do is either false or correct