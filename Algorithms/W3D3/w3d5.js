/* 
  String: Is Palindrome
  Create a function that returns a boolean whether the string is a strict palindrome. 
    - palindrome = string that is same forwards and backwards
  
  Do not ignore spaces, punctuation and capitalization
 */

// const str1 = "a x a";
// const expected1 = true;

// const str2 = "racecar";
// const expected2 = true;

// const str3 = "Dud";
// const expected3 = false;

// const str4 = "oho!";
// const expected4 = false;

function isPalindrome(str) {
  len = str.length;
  for (var i = 0; i < len / 2; i++) {
    if( str[i] !== str[len - 1 - i]) {
      console.log("not a palindrome")
      return false
    }
  }
  console.log("is a palindrome")
  return true;
}

isPalindrome("racecar")
/*****************************************************************************/

/* 
    Longest Palindrome
    For this challenge, we will look not only at the entire string provided, but also at the substrings within it. Return the longest palindromic substring. 
    Strings longer or shorter than complete words are OK.
    All the substrings of "abc" are:
    a, ab, abc, b, bc, c
*/

// const str1 = "what up, daddy-o?";
// const expected1 = "dad";

// const str2 = "uh, not much";
// const expected2 = "u";

// const str3 = "Yikes! my favorite racecar erupted!";
// const expected3 = "e racecar e";

function longestPalindromicSubstring(str) {
  var max_length = 0;
  var max_pal = '';
  for(var i = 0; i < str.length; i++) {
    var sub = str.substr(i, str.length);
    for(var j = sub.length; j >= 0; j--) {
      var sub_sub_str = sub.substr(0, j);
      if (sub_sub_str.length <= 1)
      continue;

      if(isPalindrome(sub_sub_str)) {
        if(sub_sub_str.length > max_length) {
          max_length = sub_sub_str.length;
          max_pal = sub_sub_str
        }
      }
    }
  }
  return max_pal;
}
console.log(longestPalindromicSubstring("Yikes! my favorite racecar erupted!"))

