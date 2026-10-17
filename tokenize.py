from string import whitespace, digits
from typing import List, Optional
from models import CharType, Char, Token, charTypeToTokenType


def is_char_type_single_character_type(type: CharType):
    return type in [CharType.OPEN_PARENTHESIS, CharType.CLOSED_PARENTHESIS]

def tokenize(input_string: str):
    current_token = []
    tokens = []

    for char in input_string:
        char_type = get_char_type(char)

        if char_type == CharType.WHITESPACE:
            if len(current_token) == 0:
                continue

            token = combine_chars_into_token(current_token)
            current_token = []

            if token is None:
                print(f"Empty token ignored: {token}")
            else:
                # Append new token
                tokens.append(token)

            continue

        if len(current_token) != 0:
            if char_type == current_token[-1].type and not is_char_type_single_character_type(char_type):
                current_token.append(Char(char, char_type))
            elif is_char_type_single_character_type(char_type):
                    token = combine_chars_into_token(current_token)
                    current_token = [Char(char, char_type)]

                    # Append new token
                    tokens.append(token)

        else:
            current_token.append(Char(char, char_type))

            if is_char_type_single_character_type(char_type):
                token = combine_chars_into_token(current_token)
                current_token = []

                # Append new token
                tokens.append(token)

    # Append final token
    if len(current_token) != 0:
        token = combine_chars_into_token(current_token)
        current_token = []
        tokens.append(token)

    return tokens

def combine_chars_into_token(chars: List[Char]) -> Optional[Token]:
    if len(chars) == 0:
        return None

    first_char_type = chars[0].type 
    if all(char.type == first_char_type for char in chars[1:]) and first_char_type != CharType.WHITESPACE:
        value = "".join(map(lambda c: c.char, chars))

        return Token(value, charTypeToTokenType[first_char_type])
    else:
        return None

def get_char_type(char: str):
    if char in whitespace:
        return CharType.WHITESPACE
    elif char in digits:
        return CharType.DIGIT
    elif char in "+-":
        return  CharType.BINARY_OPERATOR
    elif char in "(":
        return  CharType.OPEN_PARENTHESIS
    elif char in ")":
        return  CharType.CLOSED_PARENTHESIS

