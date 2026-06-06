<!-- Getting input from the user -->

1. What does the `input()` function do? What data type does it always return — even if the user types 42?
The `input()` function waits for the user to type something. It always returns that text as a string data type, meaning even if the user types `42`, Python reads it as the text `"42"` instead of a number.

2. Why do we often wrap `input()` in `int(...)` or `float(...)`? What goes wrong if we forget to?
We wrap `input()` in `int()` or `float()` to convert the user's text into an actual number so we can perform mathematical calculations with it. If we forget to do this, Python will throw an error when we try to do math on text.

3. What does the `type()` function tell you, and why is it handy when something is not behaving the way you expect?
The `type()` function tells you the exact data type of a value or variable (such as `str`, `int`, `float`, or `bool`). It is incredibly handy for debugging because it helps you uncover hidden type mismatches, such as discovering that a variable you think is a number is actually being treated as text by Python.

<!--  Working with strings -->

4. What do the string methods `.upper()`, `.lower()`, and `.strip()` each do? Give a short example for one of them.
`.upper()` converts all characters to uppercase.
`.lower()` converts all characters to lowercase.
`.strip()` removes any accidental spaces from the very beginning and very end of a string.
*Example:* `"  nino  ".strip()` outputs `"nino"`.

5. What do the escape sequences `\n` and `\t` mean inside a string?
These sequences represent special formatting characters: `\n` forces the text following it to start on a new line, while `\t` inserts a horizontal tab space.

<!-- Booleans and truthiness -->

6. A comparison like `age >= 18` produces a value. What data type is that value?
A comparison produces a Boolean (`bool`) data type, which can only evaluate to either `True` or `False`.

7. Why is `bool("")` False, but `bool("0")` and `bool(" ")` are both True?
In Python, strings are considered "truthy" if they contain content and "falsy" if they are completely empty. Because `""` contains absolutely nothing, it evaluates to `False`; however, `"0"` and `" "` both contain characters (a character zero and a space character), making them non-empty strings which evaluate to `True`.

<!-- Floats and constants -->

8. Why does `0.1 + 0.2 == 0.3` print False? What is `round()` useful for here?
Computers store floating-point numbers in binary format, which cannot perfectly represent certain decimal fractions, resulting in tiny, microscopic rounding errors (like `0.30000000000000004`). The `round()` function is useful here because it lets us limit the decimal precision, helping us check if the numbers are equal up to a reasonable number of decimal places.

9. Some programmers write names like `MAX_SCORE` in ALL_CAPS. What does that naming convention signal to other programmers, and why shouldn't you change such a value later?
An `ALL_CAPS` variable name signals that the value is intended to be a constant, meaning it should remain fixed and unchanged. 