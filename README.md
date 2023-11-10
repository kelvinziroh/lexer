# Python Lexer For C Source Code
## Introduction
Compiler desing is an intricate process composed of several phases of computation from lexical analysis to code generation each phase serving a specific purpose in transforming code of a particular programming language into its correspondent machine code. Below is a quick overview of each phase and its equivalent function in the compilation process. 

| Phase                        | Goal to be achieved in the phase                                                                                |
|------------------------------|-----------------------------------------------------------------------------------------------------------------|
| Lexical Analysis (Scanner)   | Breaks the source code up into a sequence of tokens                                                             |
| Syntax Analysis (Parser)     | Builds the syntactic structure of the source code using the tokens generated in the lexical analysis phase.     |
| Semantic Analysis            | Validates the meaning of the source code against that of the programming language's semantics.                  |
| Intermediate Code Generation | Converts the source code into an intermediate representation that is independent of the machine's architecture. |
| Code Optimization            | Improves the intermediate code to make the final machine code more efficient.                                   |
| Code Generation              | Translates the optimized intermediate code into machine code for the target architecture.                       |

## Python Lexer Implementation
In the following mini-project, we have focused on creating a comprehensive lexer using the python programming language. The lexer should be able to consume programs written in the C programming language and produce tokens and identify unknown characters in the source code.

The lexer leverages the power of two modules to make the lexer work efficiently.
- re module - the regular expressions module to match specific patterns within the source code
- sys module - the system-specific parameters and functions module used to provide access to variables in the terminal which in turn allows us to read files written in C.

To implement the lexer, we first import the two modules mentioned above:
```python
import re
import sys
```

We then create a class `Token` to hold information about each identified token. The class has a constructor that initializes the token with a type and a value like so:
```python
class Token:
    def __init__(self, token_type, value):
        self.type = token_type
        self.value = value

    def __str__(self):
        return f"Token({self.type}, {repr(self.value)})"
```
The `__str__` method in the `Token` class returns a human-readable string representation.

Next we implement the `Lexer` class where the actual lexical analysis actually happens. It is initialized with the source code, keeps track of the current position in the source code and an empty list of identified tokens to store the identified tokens as the lexer traverses the source code.
```python
class Lexer:
    def __init__(self, source_code):
        self.source_code = source_code
        self.position = 0
        self.tokens = []
```

We Then add a `tokenize` method which is the main function for tokenizing the source code. It traverses the source code character by character, skipping whitespaces. Depending on the type of the current character (alphabetical, numerical, or an operator), it calls specific helper methods to identify and create tokens. If a character doesn't match any expected pattern, it prints an error message and moves to the next character.
```python
def tokenize(self):
    ...
```

As discussed above, we mentioned that the `Lexer` class employs the `tokenize` method which in turn calls helper functions to identify and create different types of tokens. Some of these helper functions make use of regular expressions like so:
```python
    def tokenize_identifier_or_keyword(self):
        identifier = re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*', self.source_code[self.position:])
        if identifier:
            self.position += identifier.end()
            return Token('IDENTIFIER', identifier.group())
        return None
```
The helper function above is used to select identifiers as the lexer traverses through the source code and it uses the regular expressions defined as so:
```python
re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*', self.source_code[self.position:])
```

We didn't have to imploy regular expressions for all helper functions. For instance, the helper function for identifying operators simply needed a list to validate against like so:
```python
    def tokenize_operator(self):
        operators = ['+', '-', '*', '/', '=', '==', '!=', '<', '>', '<=', '>=']
        for op in operators:
            if self.source_code.startswith(op, self.position):
                self.position += len(op)
                return Token('OPERATOR', op)
        return None
```

We've compatmentalized the helper functions according to the types of tokens that can be identified as per the list below:
- Identifiers or keywords
- Numerical literals
- String literals
- Single line comments
- Multi line comments
- Operators

Lastly we created a main function that carries out the rest of the operations in the lexer like manipulating parts of the python runtime function using the `sys` module that we imported earlier in order to access the file to consumed by the lexer. We did this by running the following code:
```python
filename = sys.argv[1]
```


## Python Lexer Usage
We built the lexer in such a way that it would be easy to use. Below are steps to follow to get a clone of the python lexer implementation and use the python lexer:
- Click on the **Download ZIP** button if you're not familiar with the terminal.
- Open a terminal preferably any linux terminal i.e (BASh, zsh, etc). 
- Navigate to a desired directory.
- Run the following command:
`git clone git@github.com:kelvinziroh/lexer.git` if git is set up with **ssh** in your local environment
`git clone https://github.com/kelvinziroh/lexer.git` if git is set up with **https** in your local environment
- Navigate into the **lexer** directory
- Type in the following command to run the `lexer.py` script on the `sample.c` C source code
`python lexer.py sample.c`

> **NOTE:** You can run the `lexer.py` script using the version of python installed in your local environment if the version is specifically required like so:
```
python3 lexer.py sample.c
```
