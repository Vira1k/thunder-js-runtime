# Thunder JS Runtime

A lightweight JavaScript runtime built in **Python** for **Thunder Hackathon 2.0**.

## Overview

This project executes JavaScript code from a `.js` file and prints the output to the console.

The runtime uses:

* Tokenizer / Lexer
* Parser (AST-based execution)
* Tree-walk interpreter
* Function execution environment
* Scope handling

## Features Supported

### Variables

* `let`
* `const`
* reassignment
* `+=`

### Data Types

* numbers
* strings
* booleans

### Operators

* Arithmetic: `+`, `-`, `*`, `/`, `%`, `**`
* Comparison: `===`, `!==`, `==`, `!=`, `<`, `>`, `<=`, `>=`
* Logical: `&&`, `||`

### Control Flow

* `if / else`
* `while`
* `for` loops

### Functions

* Function declarations
* Function calls
* Parameters
* `return`
* Recursion

### Built-in Support

* `console.log()`
* `Math.floor()`
* `.length`

## Project Structure

```txt
thunder-js-runtime/
│── interpreter.py
│── main.py
│── test.js
│── README.md
```

## Installation

Clone repository:

```bash
git clone https://github.com/Vira1k/thunder-js-runtime.git
cd thunder-js-runtime
```

## Run

Execute JavaScript file:

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

## Hackathon Submission

Built for **Thunder Hackathon 2.0 – Build Your Own JavaScript Runtime**
