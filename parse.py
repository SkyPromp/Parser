from typing import Optional

from models import AST, TokenType


def parse(ast: AST) -> Optional[int]:
    # if ast.value.type != TokenType.ROOT and ast.value is None:
    #     return None

    print("PARSE", ast)

    match ast.value.type:
        case TokenType.DIGIT:
            return int(ast.value.value)
        case TokenType.BINARY_OPERATOR:
            if len(ast.children) != 2:
                print("ERROR in parse: Incorrect amount of children for binary operation", ast)

                return None

            match ast.value.value:
                case "+":
                    return parse(ast.children[0]) + parse(ast.children[1])
                case "-":
                    return parse(ast.children[0]) - parse(ast.children[1])
                case _:
                    print("ERROR in parse: Unknown operator type", ast.value)
        case _:
            print("ERROR in parse: Could not parse AST. Unknown token type", ast.value)

            return None
