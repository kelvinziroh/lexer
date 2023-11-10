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

    # Match valid identifiers or keywords
    def tokenize_identifier_or_keyword(self):
        identifier = re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*', self.source_code[self.position:])
        if identifier:
            self.position += identifier.end()
            return Token('IDENTIFIER', identifier.group())
        return None
    
    # Match numerical literals
    def tokenize_literal(self):
        literal = re.match(r'^\d+', self.source_code[self.position:])
        if literal:
            self.position += literal.end()
            return Token('LITERAL', int(literal.group()))
        return None
    
    # Match any predifined operator characters
    def tokenize_operator(self):
        operators = ['+', '-', '*', '/', '=', '==', '!=', '<', '>', '<=', '>=']
        for op in operators:
            if self.source_code.startswith(op, self.position):
                self.position += len(op)
                return Token('OPERATOR', op)
        return None