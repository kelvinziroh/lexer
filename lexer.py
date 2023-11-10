# Import the regular expressions module
import re

# Store information about each identified token
class Token:
    def __init__(self, token_type, value):
        self.type = token_type
        self.value = value

    def __str__(self):
        return f"Token({self.type}, {repr(self.value)})"

# Implement the lexer
class Lexer:
    def __init__(self, source_code):
        self.source_code = source_code
        self.position = 0
        self.tokens = []
    
    def tokenize(self):
        while self.position < len(self.source_code):
            char = self.source_code[self.position]

            # Skip whitespace
            if char.isspace():
                self.position += 1
                continue

            # Check for keywords, identifiers and literals
            if char.isalpha():
                token = self.tokenize_identifier_or_keyword()
            elif char.isdigit():
                token = self.tokenize_literal()
            else:
                token = self.tokenize_operator()
            
            if token:
                self.tokens.append(token)
            else:
                print(f"Error: Invalid character '{char}' at position {self.position}")
                self.position += 1

        return self.tokens