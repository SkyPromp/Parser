from typing import List, Optional
from models import Token, TokenType, AST


def create_AST(tokens: List[TokenType]) -> Optional[AST]:
    ast_tree = AST(Token("", TokenType.ROOT), [])
    parenthesis_level = 0
    parenthesis_tokens = []

    for token in tokens:
        print("CURRENT TOKEN:", token, "PARENTHESIS_LEVEL:", parenthesis_level, "PARENTHESIS_TOKENS", parenthesis_tokens)

        if parenthesis_level > 0:
            if token.type == TokenType.CLOSED_PARENTHESIS:
                parenthesis_level -= 1

                if parenthesis_level < 0:
                    print("ERROR in create_AST: Parenthesis closed before opening", ast_tree, token)

                    return None
                elif parenthesis_level == 0:
                    sub_ast = create_AST(parenthesis_tokens)
                    parenthesis_tokens = []

                    if sub_ast.value.type == TokenType.ROOT:
                        sub_ast = sub_ast.children

                        if len(sub_ast) != 1:
                            print("ERROR in create_AST: Unexpected amount of children in sub AST", sub_ast)

                            return None

                        sub_ast = sub_ast[0]

                    ast_tree.append_child(sub_ast)

                    continue

            parenthesis_tokens.append(token)
            print("Parenthesis level:", parenthesis_level, "Parenthesis tokens:", parenthesis_tokens)

            continue

        match token.type:
            case TokenType.DIGIT: # Check that it's parent has the correct amount of children and check that digit has no children
                node = AST(token, None)
                ast_tree.append_child(node)
                # ast_tree.children.append(node)
            case TokenType.BINARY_OPERATOR:  # TODO: Check for empty left side
                if ast_tree.value.type == TokenType.ROOT:
                    ast_tree = AST(token, ast_tree.children)
                else:
                    ast_tree = AST(token, [ast_tree])
            case TokenType.OPEN_PARENTHESIS:
                parenthesis_level += 1
            case TokenType.CLOSED_PARENTHESIS:
                print("ERROR in create_AST: Parenthesis closed before opening", ast_tree, token)

                return None
            case _:
                print("Unknown token type:", token)

        print("-"*10)
        print(ast_tree)
        print("-"*10)

    return ast_tree

