/* 
Given a SORTED array of integers, dedupe the array 
Because array elements are already in order, all duplicate values will be grouped together.
Ok to use a new array
Bonus: do it in O(n) time (no nested loops, new array ok)
*/

const nums1 = [1, 1, 1, 1];
const expected1 = [1];

const nums2 = [1, 1, 2, 2, 3, 3];
const expected2 = [1, 2, 3];

const nums3 = [1, 1, 2, 3, 3, 4];
const expected3 = [1, 2, 3, 4];

// function dedupeSorted(nums) {
//     newArr = [];
//     for (let i = 0; i <= nums.length; i++) {
//         if (nums[i] = nums[i + 1]) {
//             newArr.push(nums[i]);
//         }else if(nums[i] != nums[i + 1]) {
//             return false
//         }
//     }
// }
// console.log(dedupeSorted(nums1))

function dedupeSorted(nums) {
    var seen = {};
    var out = [];
    var len = nums.length;
    var j = 0;
    for (let i = 0; i < len; i++) {
        var item = nums[i];
        if (seen[item] !== 1) {
            seen[item] = 1;
            out[j++] = item;
        }
    }
    return out;
} 
console.log(dedupeSorted(nums1))
console.log(dedupeSorted(nums2))
console.log(dedupeSorted(nums3))
/*****************************************************************************/

/* 
Array: Mode

Create a function that, given an array of ints,
returns the int that occurs most frequently in the array.
What if there are multiple items that occur the same number of time?
- return all of them (in an array)
- what if all items occur the same number of times?
- return empty array
*/

const nums1 = [];
const expected1 = [];

const nums2 = [1];
const expected2 = [1];

const nums3 = [5, 1, 4];
const expected3 = [];

const nums4 = [5, 1, 4, 1];
const expected4 = [1];

const nums5 = [5, 1, 4, 1, 5];
const expected5 = [5, 1];
//  - order doesn't matter

// function mode(nums) {
//     var newArray = [];
//     var len = nums.length;
//     var counter = 0;
//     for (let i = 0; i < len; i++) {
//         for(let j = len - 1; j >= len - 1; j--) {
//             if (nums[i] == nums[j]) {
//                 newArray.push(nums[i]);

//             } else if (nums[i] !== nums[j]) {
//                 continue;
//             }
//         }
//     }
//     return newArray;
// }

// console.log(mode(nums5))