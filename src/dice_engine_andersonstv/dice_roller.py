from tokenizer import tokenize
from parser import parse_and_eval

def roll_with_result(dice_expression):
    tokens = tokenize(dice_expression)
    return parse_and_eval(tokens)

def roll(dice_expression):
    _, total = roll_with_result(dice_expression)
    return total
