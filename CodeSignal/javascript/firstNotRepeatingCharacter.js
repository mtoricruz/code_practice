// Given a string s consisting of small English letters, 
// find and return the first instance of a non-repeating character in it. 
// If there is no such character, return '_'.

// EXAMPLE
// For s = "abacabad", the output should be
// firstNotRepeatingCharacter(s) = 'c'.

// Understand
// given a STRING of lowercase letters
// Find/return the FIRST instance of a non-repeating character
// If no uniques, return '_'

// Plan


// Execute

const string = 'abaabaed'

function firstNotRepeatingCharacter(s) {
    // looping through length of string
    for(let i=0; i<s.length; i++){
        // if the last index of a given element is === the current index of a given element
        // a unique letter can be determined by if the last index it appears at is equal to the current index 
        if(s.lastIndexOf(s[i]) === s.indexOf(s[i])){
            // return that element
            return s[i];
        } 
    }
    // return '_' if no unique is found
    return '_'
}

console.log(firstNotRepeatingCharacter(string))