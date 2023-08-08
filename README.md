# dice-engine
A simple engine for simulating dice rolls.

The purpose of this package is to handle dice expressions, from parsing to generating numbers. It can be run from a command-line interface or used in other applications.



# Dice Notation
This software handles dice rolling in the form of dice expressions. The dice expressions recognized follow the following form: 

*AdX*

A = Number of dice being rolled.
X = Number of sides of each dice.

More can read about Dice notation [here](https://en.wikipedia.org/wiki/Dice_notation)

Currently the software supports some basic operations:
+/- : Sum and subtraction between dice and/or integers.

Example of valid expressions:
 - *1d20 + 3*
 - *3d6 + 1d6*
 - *2d8 - 1d4 + 3*

# Dice Roller

To simulate a dice roll:

```
my_dice_expression = "2d6+ 3"
total = dice_engine.roll(my_dice_expression)

print(total)

## 8
```

```
my_dice_expression = "2d6+ 3"
result, total = dice_engine.roll_with_result(my_dice_expression)

print(result)
print(total)

## 2d6(4, 1) + 3
## 8
```

## Dice Parser

If you want to implement your own operations and methods, you can also use the tokenizer and parser included.

Tokenizer:
 - `tokenize(expression)` : Receives a dice expression as a string and returns a list of tokens. Ex: [("2d10", "DICE), ("+", "OPERATOR"), (2, "NUMBER")]
 - `reconstruct(tokens)` : Reconstruct a dice expression from a list of tokens.

 Parser:
  - `parse(tokens)` : Parses a list of tokens and builds a AST from it.
  - `parse_and_eval(expression)` : Parses a list of tokens and evaluates the result.
