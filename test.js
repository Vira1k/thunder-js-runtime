// ==============================================================================
// 🏆 THUNDER HACKATHON 2.0 - MANDATORY TEST CASES (TC-1 to TC-5)
// ==============================================================================

// TEST CASE 1: Odd / Even Checker (20 Points)
let num = 7; 
if (num % 2 === 0) { 
    console.log(num + " is Even"); 
} else { 
    console.log(num + " is Odd"); 
}

// TEST CASE 2: Triangle Pattern using For Loop (20 Points)
for (let i = 1; i <= 5; i++) { 
    let row = ""; 
    for (let j = 1; j <= i; j++) { 
        row += "*"; 
    } 
    console.log(row); 
}

// TEST CASE 3: Armstrong Number (20 Points)
function isArmstrong(num) { 
    let temp = num; 
    let sum = 0; 
    while (temp > 0) {
        let digit = temp % 10;
        sum += digit ** 3;
        temp = Math.floor(temp / 10);
    }
    return sum === num;
} 
console.log(isArmstrong(153));
console.log(isArmstrong(123));

// TEST CASE 4: Array Reverse (20 Points)
let arr = [1, 2, 3, 4, 5]; 
let reversed = [...arr].reverse(); 
console.log("Original: " + arr.join(", ")); 
console.log("Reversed: " + reversed.join(", "));

// TEST CASE 5: String Palindrome Check (20 Points)
let str = "racecar"; 
let strReversed = str.split("").reverse().join(""); 
if (str === strReversed) { 
    console.log(str + " is a Palindrome"); 
} else { 
    console.log(str + " is not a Palindrome"); 
}

// ==============================================================================
// ⚡ CORE INTERPRETER STABILITY & ENGINE VALIDATION TESTS
// ==============================================================================

// TEST 6: Basic Operator Precedence Matrix
let a = 10 + 5 * 2;
let b = Math.floor(15 / 2);
console.log(a);
console.log(b);

// TEST 7: Parentheses Brackets Tree Resolution
let bracketRes = (5 + 3) * 2;
console.log(bracketRes);

// TEST 8: Negative Numbers Operations
let negativeNum = -10 + 25;
console.log(negativeNum);

// TEST 9: String Literals Sequential Concatenation
let first = "John";
let last = "Doe";
let combined = first + " " + last;
console.log(combined);

// TEST 10: Strict Equality Validation Blocks
let x = 10;
let y = 20;
console.log(x === y);
console.log(x < y);
console.log(x <= 10);

// TEST 11: Standard Inline Loop Control Structure
let count = 1;
while (count <= 3) {
    console.log("Count is: " + count);
    count += 1;
}

// TEST 12: Multi-line Syntax Formatting Loops
let loopVar = 1;
while (loopVar < 3) {
    console.log("Multi-line structure val: " + loopVar);
    loopVar += 1;
}

// TEST 13: Custom Function execution with Exponentiation
function power(base, exp) {
    return base ** exp;
}
let powerRes = power(2, 3);
console.log(powerRes);

// TEST 14: Commas protection inside String Arguments Tokens
function greet(msg) {
    return "Message received: " + msg;
}
console.log(greet("Hello, Developer"));

// TEST 15: Scope Shadowing Frame Isolation
let scopedNum = 50; 
function checkScope(scopedNum) {
    return scopedNum + 10;
}
console.log(checkScope(5));
console.log(scopedNum);

// TEST 16: Global Variable state modification inside function block
let globalValue = 10;
function mutateGlobal() {
    globalValue = 99;
}
mutateGlobal();
console.log(globalValue);

// TEST 17: Conditional If-Else Branching Tree
let age = 18;
if (age >= 18) {
    console.log("Allowed");
} else {
    console.log("Not Allowed");
}

// TEST 18: Logical Short-Circuit Operators (AND / OR Evaluation)
let score = 85;
let passed = (score > 50 && score <= 100);
console.log(passed);

// TEST 19: Hard Nesting Floating Arithmetic Precision 
let decimalCalc = 0.5 * (10.5 + 4.5) - -2;
console.log(decimalCalc);

// TEST 20: String Native Length Property Mapping
let username = "ThunderJS";
console.log(username.length);

// TEST 21: Deep Functional Recursion Stack
function factorial(n) {
    if (n === 1) {
        return 1;
    }
    return n * factorial(n - 1);
}
console.log("Factorial of 5 is:", factorial(5));

// TEST 22: Multi-Variable Nested Conditional Mapping
let hours = 14;
if (hours < 12) {
    console.log("Good Morning");
} else {
    if (hours < 18) {
        console.log("Good Afternoon");
    } else {
        console.log("Good Evening");
    }
}