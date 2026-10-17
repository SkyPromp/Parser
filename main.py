from tokenize import tokenize
from AST import create_AST
from parse import parse

# input_string = "8 + ( 9 + 10 ) + 11"  # 38
# input_string = "9 + 10"  # 19
# input_string = "10 - 9"  # 1
# input_string = "10 - ( 9 - 3 )"  # 4
# input_string = "10 - ( 9 + 3)"  # -2
# input_string = "10 - (( 9 + 3))"  # -2 (BREAKS)
input_string = "10 - ( 1 + ( 9 + 3))"  # -3 (BREAKS)
print(f"Input string: {input_string}")
tokens = tokenize(input_string)
print("TOKENS", tokens)
ast = create_AST(tokens)
print("AST", ast)
print("PARSED:", parse(ast))

