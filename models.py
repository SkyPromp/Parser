from __future__ import annotations
from enum import Enum
from dataclasses import dataclass
from typing import List, Optional

class CharType(Enum):
    WHITESPACE = 1
    DIGIT = 2
    BINARY_OPERATOR = 3
    OPEN_PARENTHESIS = 4
    CLOSED_PARENTHESIS = 5

@dataclass
class Char:
    char: str
    type: CharType

class TokenType(Enum):
    DIGIT = 1
    BINARY_OPERATOR = 2
    OPEN_PARENTHESIS = 3
    CLOSED_PARENTHESIS = 4

    def __str__(self) -> str:
        return self.name

@dataclass
class Token:
    value: str
    type: TokenType

    def __repr__(self) -> str:
        return f"<{self.value}:{self.type}>"

charTypeToTokenType = { 
    CharType.DIGIT: TokenType.DIGIT,
    CharType.BINARY_OPERATOR: TokenType.BINARY_OPERATOR,
    CharType.OPEN_PARENTHESIS: TokenType.OPEN_PARENTHESIS,
    CharType.CLOSED_PARENTHESIS: TokenType.CLOSED_PARENTHESIS
}

@dataclass
class AST:
    value: Optional[Token]
    children: Optional[List[AST]]

    def __repr__(self) -> str:
        if self.value is None:
            if self.children is None:
                return "{ }"
            else:
                return f"{{}}: [{self.children}]"

        if self.children is None:
            return f"{self.value}"

        return f"{self.value}: [{self.children}]"

