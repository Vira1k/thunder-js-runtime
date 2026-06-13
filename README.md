# Thunder JS Runtime

A JavaScript runtime built in Python for **Thunder Hackathon 2.0**.

## Overview

This project executes JavaScript code from a `.js` file and prints the output to the console.

The runtime supports:

- Variables (`let`, `const`)
- Functions
- Conditional statements (`if`, `else`)
- Loops (`for`, `while`)
- Arithmetic operations
- Arrays
- Strings
- `console.log()`

## Project Structure

```txt
thunder-js-runtime/
│── interpreter.py
│── main.py
│── README.md
│── requirements.txt
│── test.js
```

## How to Run

### 1. Clone Repository

```bash
git clone <your-repo-link>
cd thunder-js-runtime
```

### 2. Run

```bash
python main.py test.js
```

## Example

### Input (`test.js`)

```js
let num = 7;

if (num % 2 === 0) {
    console.log(num + " is Even");
} else {
    console.log(num + " is Odd");
}
```

### Output

```txt
7 is Odd
```

## Hackathon

Submission for **Thunder Hackathon 2.0 – Build Your Own JavaScript**