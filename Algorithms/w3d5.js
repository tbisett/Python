/* 
Given an int to represent how much change is needed
calculate the fewest number of coins needed to create that change,
using the standard US denominations
*/

const cents1 = 25;
const expected1 = { quarter: 1 };

const cents2 = 50;
const expected2 = { quarter: 2 };

const cents3 = 9;
const expected3 = { nickel: 1, penny: 4 };

const cents4 = 99;
const expected4 = { quarter: 3, dime: 2, penny: 4 };

function fewestCoinChange(cents) {
    let coins= {};
    let quarters = Math.floor(cents/25)
    if (quarters >0) coins['quarter'] = quarters;

    cents = cents - quarters*25;
    let dimes = Math.floor(cents/10);
    if (dimes > 0) coins['dime'] = dimes;
    cents = cents - dimes * 10;
    let nickles = Math.floor(cents/5)
    if (nickles > 0) coins['nickle'] = nickles;
    cents = cents - nickles * 5;
    if (cents > 0) coins['penny'] = cents;
    return coins;
}

console.log(fewestCoinChange(cents1))
console.log(fewestCoinChange(cents2))
console.log(fewestCoinChange(cents3))
console.log(fewestCoinChange(cents4))
/*****************************************************************************/

/* 
Missing Value
You are given an array of length N that contains, in no particular order,
integers from 0 to N . One integer value is missing.
Quickly determine and return the missing value.
*/


const nums1 = [3, 0, 1];
const expected1 = 2;

const nums2 = [3, 0, 1, 2];
const expected2 = null;
// Explanation: nothing is missing

function missingValue(unorderedNums) {

let missingNum = null;
let lowest = unorderedNums[0];
let highest = unorderedNums[0];

for(let i = 0; i<unorderedNums.length;i++){
    if(lowest> unorderedNums[i]) lowest = unorderedNums[i];
    if(highest<unorderedNums[i]) highest = unorderedNums[i]; 
}

for (let i = lowest; i<=highest; i++){
    if (!unorderedNums.includes(i)) missingNum = i;
}


return missingNum;
}

console.log(missingValue(nums1))
console.log(missingValue(nums2))