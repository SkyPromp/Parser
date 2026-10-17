from typing import List
from models import TokenType, AST


def create_AST(tokens: List[TokenType]):
    ast_tree = AST(None, [])

    for token in tokens:
        node = AST(token, None)
        ast_tree.children.append(node)

    print(ast_tree)

