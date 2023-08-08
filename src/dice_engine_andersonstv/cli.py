from .src/dice-engine import roll_with_result

print("Write your dice expression and press Enter:")
exp = input()

res, total = roll_with_result(exp)
print(res)
print(total)
