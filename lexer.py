# Import the regular expressions module
import re
import sys


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
        identifier = re.match(
            r"^[a-zA-Z_][a-zA-Z0-9_]*", self.source_code[self.position :]
        )
        if identifier:
            self.position += identifier.end()
            return Token("IDENTIFIER", identifier.group())
        return None

    # Match numerical literals
    def tokenize_literal(self):
        literal = re.match(r"^\d+", self.source_code[self.position :])
        if literal:
            self.position += literal.end()
            return Token("LITERAL", int(literal.group()))
        return None
    
    # Match string literals
    def tokenize_string_literal(self):
        string_literal = re.match(r'^"([^"\\]|\\.)*"', self.source_code[self.position:])
        if string_literal:
            self.position += string_literal.end()
            return Token('STRING_LITERAL', string_literal.group())
        return None
    
    # Match single line comments
    def consume_single_line_comment(self):
        end_of_line = self.source_code.find('\n', self.position)
        if end_of_line == -1:
            self.position = len(self.source_code)
        else:
            self.position = end_of_line
    
    # Match multi-line comments
    def consume_multi_line_comment(self):
        end_of_comment = self.source_code.find('*/', self.position + 2)
        if end_of_comment == -1:
            print("Error: Unterminated multi-line comment")
            self.position = len(self.source_code)
        else:
            self.position = end_of_comment + 2

    # Match any predifined operator characters
    def tokenize_operator(self):
        operators = ["+", "-", "*", "/", "=", "==", "!=", "<", ">", "<=", ">="]
        for op in operators:
            if self.source_code.startswith(op, self.position):
                self.position += len(op)
                return Token("OPERATOR", op)
        return None


# Read files to perform lexical analysis
def main():
    # Check if the terminal argument is valid
    if len(sys.argv) != 2:
        sys.exit("Usage: python lexer.py <filename>")

    # Get the file
    filename = sys.argv[1]

    try:
        # Open the file in read mode
        with open(filename, "r") as file:
            source_code = file.read()
    except FileNotFoundError:
        # Raise FileNotFoundError if the file specified is not found
        sys.exit(f"Error: File '{filename}' not found.")

    # Create a lexer object and tokenize it
    lexer = Lexer(source_code)
    tokens = lexer.tokenize()

    # Display each token produced from the source code
    for token in tokens:
        print(token)


# Call main function
if __name__ == "__main__":
    main()
