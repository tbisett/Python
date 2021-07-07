function acronymize(str) {
    var wordsArr = str.split(" ");
    var newArr = [];
    for(var i = 0; i < wordsArr.length; i++) {
        newArr.push(wordsArr[i].charAt(0).toUpperCase())
    }
    return newArr.join(' ');
}
console.log(acronymize("Live from New York, it's Saturday Night!"));
console.log(acronymize("there's no free lunch - gotta pay yer way"));



const str1 = "creature";
const str2 = "dog";


function reverseString(str) {
    // empty sting variable to store the reveresed string
    var reversed = ""; 
    
    // i iterates through the original string from the last letter to the first and adds each i iteration to the reversed string
    for(var i = str.length -1; i >= 0; i--) {
        reversed += str[i];
    }
    // gives the new string to var reversed
    return reversed;
}

console.log(reverseString(str1))