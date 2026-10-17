from tokenize import tokenize
from AST import create_AST
from parse import parse



def runTests():
    testEndToEnd("8 + ( 9 + 10 ) + 11", 38)
    testEndToEnd("9 + 10", 19)
    testEndToEnd("10 - 9", 1)
    testEndToEnd("10 - ( 9 - 3 )", 4)
    testEndToEnd("10 - ( 9 + 3)", -2)
    testEndToEnd("10 - (( 9 + 3))", -2)
    testEndToEnd("10 - ( 1 + ( 9 + 3))", -3)

def testEndToEnd(input_string: str, expected_outcome: int):
    print(f"Running: {input_string} == {expected_outcome}")
    tokens = tokenize(input_string)
    ast = create_AST(tokens)
    outcome = parse(ast)

    if outcome == expected_outcome:
        print("Success")

        return True
    else:
        print(f"Failed test outcome {outcome} does not equal expected outcome {expected_outcome} for {input_string}")
        print("TOKENS", tokens)
        print("AST", ast)
        print("------")

        return False
