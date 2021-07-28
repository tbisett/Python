function multArr(arr) {
    // BASE CASE
    if (arr.length < 2) return arr[0];
    // FORWARD PROGRESS
    // RECURSIVE CALL
  
    num = arr[0] // first thing in the arr
    newArr = arr.slice(1, arr.length) // grabbing everything else
  
    return num * multArr(newArr)
  }
  
  
/* 
Recursively sum an arr of ints
*/
  
  const nums1 = [1, 2, 3];
  const expected1 = 6;
  
  function sumArr(nums) {
    // BASE CASE
    // FORWARD PROGRESS
    // RECURSIVE CALL
    if (arr.length < 2) return arr[0];
    // FORWARD PROGRESS
    // RECURSIVE CALL
  
    num = arr[0] // first thing in the arr
    newArr = arr.slice(1, arr.length) // grabbing everything else
  
    return num + sumArr(newArr)
  }
  
  /*****************************************************************************/
  
/* 
Recursive Sigma
Input: integer
Output: sum of integers from 1 to Input integer
*/

const num1 = 5;
const expected1 = 15;
// Explanation: (1+2+3+4+5)
  
const num2 = 2.5;
const expected2 = 3;
// Explanation: (1+2)
  
const num3 = -1;
const expected3 = 0;


function recursiveSigma(num) {
    let i  = Math.floor(num)
    if( i <= 1)
    return i;
    return i + recursiveSigma(i - 1);

        
}



// function recursiveSigma(num) {
//     newArr = []
//     if (num < 1) return num[0];

//     newNum = num[0]

//     newArr.push(Math.floor(num[0]))

//     return num + recursiveSigma(num[0] -=  1)

    
// }
// console.log(recursiveSigma(num1))
// console.log(recursiveSigma(num2))
// console.log(recursiveSigma(num3))
