from tokenizer import tokenize, reconstruct, extract_lexeme
###import parser
from pretty_print import print_results
from parser import evaluate_dice, parse, parse_and_eval


print("Write your dice expression and press Enter:")
exp = input()


tokens = tokenize(exp)


(res, total) = parse_and_eval(tokens)
print(res)
print(total)
