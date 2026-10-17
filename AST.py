from typing import List, Optional
from models import Token, TokenType, AST


def create_AST(tokens: List[TokenType]) -> Optional[AST]:
    ast_tree = AST(Token("", TokenType.ROOT), [])

    for token in tokens:
        match token.type:
            case TokenType.DIGIT:
                node = AST(token, None)
                ast_tree.append_child(node)
                # ast_tree.children.append(node)
            case TokenType.BINARY_OPERATOR:  # TODO: Check for empty left side
                if ast_tree.value.type == TokenType.ROOT:
                    ast_tree = AST(token, [ast_tree.children])
                else:
                    ast_tree = AST(token, [ast_tree])
            # case TokenType.OPEN_PARENTHESIS:
            #     node = AST(token, None)
            #     ast_tree.append_child(node)
            #     # ast_tree.children.append(node)
            # case TokenType.CLOSED_PARENTHESIS:
            #     node = AST(token, None)
            #     ast_tree.append_child(node)
            #     # ast_tree.children.append(node)
            case _:
                print("Unknown token type:", token)

        print("-"*10)
        print(ast_tree)
        print("-"*10)

    return ast_tree

