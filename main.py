from tokenize import tokenize
from AST import create_AST

input_string = "8 + ( 9 + 10 ) + 11"
input_string = "9 + 10"
print(f"Input string: {input_string}")
tokens = tokenize(input_string)
ast = create_AST(tokens)
print(ast)

