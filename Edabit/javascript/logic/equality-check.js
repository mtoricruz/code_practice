// In this challenge, you must verify the equality of two different given parameters: a and b.

// Both the value and the type of parameters need to be tested in order to have a matching equality. The possible types of the given parameters are:

// Numbers
// Strings
// Booleans (false or true)
// Special values: undefined, null and NaN
// What have you learned so far that will permit you to do two different checks (value and type) with a single statement?

// Implement a function that returns true if the parameters are equal, and false if they are different.

// Understanding
// must compare value AND type of input for a and b parameters
// possible to check with a single statement - look this up
// return true if parameters are === and false if they're different

// Planning
// if a strictly equals b 
//      return true
// else 
//      return false

// Execute
function checkEquality(a, b) {
    if (a === b) {
        return true
    } else {
        return false
    }
}

// Refactor/Reflect
// use ternary operator
function checkEquality(a, b) {
    return ( a === b ? true : false )
}

// 1 line answer from user kewlceo
const checkEquality = (a, b) => a === b; 