---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: atomic
tags: ["m-language", "functions"]
---


# M Functions as Values

In M, a function is a value like any other. Functions are created with the `=>` (goes-to) syntax, can be stored in records and let variables, passed as arguments, and returned from other functions.

## Key Points

- A function is written: `(param1, param2) => expression`
- Functions are **values**: they can be stored, passed, and returned
- When invoked, arguments are substituted for parameters in the body
- M's library is a collection of function values
- Functions capture their lexical environment (closure)

## Examples

```m
// Function that adds two numbers
Add = (x, y) => x + y,
OnePlusOne = Add(1, 1),    // 2
OnePlusTwo = Add(1, 2),    // 3

// Function stored in a record
[
    Double = (n) => n * 2,
    Result = Double(21)     // 42
]

// Passing a function as an argument
List.Transform({1, 2, 3}, each _ * 2)  // {2, 4, 6}
```

## Related

- [[m_let_expressions]] — defining functions in let blocks
- [[m_standard_library]] — library functions are values
- [[function_invoke]] — Function.Invoke
