// https://digitalcrafts.instructure.com/courses/189/pages/javascript-101?module_item_id=23207
//! Hello You!
// function hello(name) {
//     console.log(`Hello, ${name}!`)
// }
// hello("vero")

//! Modify your hello program such that if no name is given: hello(), it will print "Hello, world!", otherwise it behaves the same as previously.
// function hello(name) {
//     if (name.length == 0) { console.log(`Hello world`) }
//     else {
//         console.log(`hello ${name}`)
//     }
// }
// hello("vero")

//!medium Madlib
// function madlib(name, subject) {
//     return `${name}'s favorite subject in school is ${subject}.`;
// }
// console.log(madlib("Anushka", "art"));



//! Tip Calculator
//? Write a function tipAmount that is given the bill amount and the level of service(one of good, fair and poor) and returns the dollar amount for the tip.Based on:
//? good -> 20 % fair -> 15 % bad -> 10 %

// function tipAmount(billAmount, service) { 
//     let result;
//     switch (service) {
//         case "good":
//             result = billAmount * 0.2
//             return result
//             break
//         case "fair":
//             result = billAmount * 0.15
//             return result
//             break
//         case "bad":
//             result = billAmount * 0.1
//             return result
//             break
//         default:
//             console.log("no no no no")
//   }
// }
// console.log(tipAmount(200, "good"))

//!Write a function totalAmount that takes the same arguments as tipAmount except it returns the total as the tip amount plus the bill amount. This function may make use of tipAmount as a sub-task.

// function totalAmount(billAmount, service) {
//     let result;
//     switch (service) {
//         case "good":
//             result = billAmount * 0.2;
//             break;
//         case "fair":
//             result = billAmount * 0.15;
//             break;
//         case "bad":
//             result = billAmount * 0.1;
//             break;
//         default:
//             console.log("no no no no");
//     }
//     total = billAmount + result;
//     return total;
// }
// console.log(totalAmount(300,"good"))

//! Write a function splitAmount that takes the bill amount and the level of service, and the number of people to split the bill between. It will return the final amount for each person.

// function splitAmount(billAmount, service,split) {
//     let result;
//     switch (service) {
//         case "good":
//             result = billAmount * 0.2;
//             break;
//         case "fair":
//             result = billAmount * 0.15;
//             break;
//         case "bad":
//             result = billAmount * 0.1;
//             break;
//         default:
//             console.log("no no no no");
//     }
//     total = billAmount + result;
//     totalBill = total / split;
//     return totalBill;
// }
// console.log(splitAmount(300,"good",3))

//! Write a function printNumbers which is given a start number and an end number. It will print the numbers from one to the other, one per line:
// function printNumbers(start, end) {
//     for (let i = start; i <= end; i++){
//         console.log(i)
//     }
// }
// console.log(printNumbers(1,10))

//! Write two versions of the above function. One using a while loop and the other using a for loop.

// function printNumbers(start, end) {
//     while (start <= end) {
//         console.log(start)
//         start++
//     }
// }
// printNumbers(1,10)

//! Write a function printSquare which is given a size and prints a square of that size using asterisks.
// function printSquare(num1) {
//     for (let i = 0; i <= num1; i++){
//         console.log("---")
//     }
// }
// printSquare(5)

//! Write function printBox which is given a width and height and prints a hollow box of those given dimensions.


//!Write a function printBanner which is given some text and prints a banner with a border surrounding the text. The border has to stretch to the length of the text.

// function printBanner(text) {
//     i=text.length;
//     console.log('-'.repeat(i));
//     console.log(`-${text}-`);
//     console.log('-'.repeat(i));
//     }
// printBanner('Welcome to DigitalCrafts')

//!Write a function leetspeak which is given a string, and returns the leetspeak equivalent of the string. To convert text to its leetspeak version, make the following substitutions:

// function leetspeak(string) {
//     let string1 = [];
//     for (let i = 0; i < string.length; i++) {
//         switch (string[i]) {
//             case "A" || "a":
//             string1.push(4);
//                 break;
//             case "e" || "E":
//             string1.push(3);
//                 break;
//             case "g" || "G":
//             string1.push(6);
//                 break;
//             case "i" || "I":
//             string1.push(1);
//                 break;
//             case "o" || "O":
//             string1.push(0);
//                 break;
//             case "s" || "S":
//             string1.push(5);
//                 break;
//             case "t" || "T":
//             string1.push(7);
//                 break;
//             default:
//             string1.push(string[i]);
//                 break;
//         }
//     }
//     return string1.join("");
// }
// console.log(leetspeak("Leet"));


//! given an array of numbers return a new array containing only the positive values
// function positiveNums(array) {
//     newArr = [];
//     for (let i = 0; i < array.length; i++) {
//         if (array[i] >= 0) {
//             newArr.push(array[i]);
//         }
//     }
//     return newArr;
// }
// console.log(positiveNums([1, -3, 5, -3, 0]));


//! long-long vowels - given a string, return a string with long vowels extended to length 5
// function longLongVowels(word) {
//     let newArr = []
//     for (let i = 0; i < word.length; i++) {
//         if (i < word.length - 1 && "aeoiu".includes(word[i])) {
//             if ("aeoiu".includes(word[i])) {
//                 newArr.push(word[i].repeat(5));
//             } else if (i < word.length - 1 && "aeoiu".includes(word[i + 1])) {
//                 newArr.push(word[i].repeat(5));
//             } else newArr.push(word[i]);
//         } else newArr.push(word[i]);
//     }
//     return newArr.join("");
// }
// console.log(longLongVowels("Good"));
// console.log(longLongVowels("Cheese"));
// console.log(longLongVowels("Man"));
// console.log(longLongVowels("min"));
// console.log(longLongVowels("mun"));


//! coder
// function caesarShift(str, amount) {
//     // Wrap the amount
//     if (amount < 0) {
//         return caesarShift(str, amount + 26);
//     }

//     // Make an output variable
//     let output = "";

//     // Go through each character
//     for (let i = 0; i < str.length; i++) {
//         // Get the character we'll be appending
//         let c = str[i];

//         // If it's a letter...
//         if (c.match(/[a-z]/i)) {
//             // Get its code
//             let code = str.charCodeAt(i);

//             // Uppercase letters
//             if (code >= 65 && code <= 90) {
//                 c = String.fromCharCode(((code - 65 + amount) % 26) + 65);
//             }

//             // Lowercase letters
//             else if (code >= 97 && code <= 122) {
//                 c = String.fromCharCode(((code - 97 + amount) % 26) + 97);
//             }
//         }

//         // Append
//         output += c;
//     }

//     return output;
// }
// console.log(caesarShift("Genius without education is like silver in the mine",4))





//! decode