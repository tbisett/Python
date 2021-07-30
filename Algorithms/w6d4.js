/* 
Recursively reverse a string
helpful methods:
str.slice(beginIndex[, endIndex])
returns a new string from beginIndex to endIndex exclusive
*/

const str1 = "abc";
const expected1 = "cba";

const str2 = "";
const expected2 = "";

function reverseStr(str) {
    let start = str[0];
    let end = str.length - 1;
    if (str == "") {
        return "";
    }else {
        return reverseStr(str.substr(1)) + str.charAt(0);
    }
    
}
console.log(reverseStr(str1))
console.log(reverseStr(str2))
/*****************************************************************************/

/*
Sum To One Digit
Implement a function sumToOne(num)​ that,
given a number, sums that number’s digits
repeatedly until the sum is only one digit. Return
that final one digit result.
Tips:
to access digits from a number, need to convert it .toString() to access each digit via index
parseInt(arg) returns arg parsed as an integer, or NaN if it couldn't be converted to an int
isNaN(arg) used to check if something is NaN
*/

const num1 = 5;
const expected1 = 5;

const num2 = 10;
const expected2 = 1;

const num3 = 25;
const expected3 = 7;

const num4 = 57;
const expected4 = 3;

const num5 = 888;
const expected5 = 6;

const num6 = "hello there";
const expected6 = null;

function sumToOneDigit(num) {
    if (num == NaN) {
        return null;
    } else {
        
    }
}
console.log(sumToOneDigit(num1))
// console.log(sumToOneDigit(num2))
// console.log(sumToOneDigit(num3))
// console.log(sumToOneDigit(num4))
// console.log(sumToOneDigit(num5))
// console.log(sumToOneDigit(num6))