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