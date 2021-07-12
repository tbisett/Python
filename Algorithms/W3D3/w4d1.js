const str1 = "aaaabbcddd";
const expected1 = "a4b2c1d3";

const str2 = "";
const expected2 = "";

const str3 = "a";
const expected3 = "a";

const str4 = "bbcc";
const expected4 = "bbcc";

function encodeStr(str) {
    var temp = [];
    var count = 0;
    for(var i = 0; i <= str.length; i++) {
        if(i == 0) {
            temp.push(str[i]);
            count ++;
        }
        else if(str[i] == str[i-1]) {
            count++;
        }
        else {
            temp.push(count);
            temp.push(str[i]);
            count = 0;
            count++;
        }
    }
    // console.log(temp.join(""))
    if(temp.length < str.length) {
        return temp.join("");
    }
    else {
        return str;
    }
}

encodeStr("bbcc")
console.log(encodeStr("bbcc"))
/*****************************************************************************/

/* 
  String Decode  
*/

const str1 = "a3b2c1d3";
const expected1 = "aaabbcddd";

function decodeStr(str) {
    let decoded = "";
    for(var i = 0; i < str.length; i++) {
        var n = parseInt(str[i])
        // str[i] is a number: n = number
        // str[i] is a letter: n = NaN

        if(n) {
            decoded += str[i - 1].repeat(n) //"a".repeat(3) => "aaa"
            
        }
    }



    return decoded
}