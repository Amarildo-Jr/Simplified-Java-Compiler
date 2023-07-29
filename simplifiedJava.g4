grammar simplifiedJava;

program: (functionsBlock)? mainFunction EOF;

functionsBlock: (function)+;

function: functionDeclaration (variableDeclarationArea)? (cmdBlock)? 'end';

functionDeclaration: ID'(' (declarationParametersList)? ')' ':' (type | 'void');

declarationParametersList: type ID (',' type ID)*;

mainFunction: 'main' ':' (variableDeclarationArea)? (cmdBlock)? 'end';

variableDeclarationArea: 'var' ':' (variableDeclaration)+;

variableDeclaration: variableList ':' type ';' |
                    'const' attributionList ';';

cmdBlock: (command)+;

command: controlCmd
         | attributionCmd ';'
         | ioCmd ';'
         | functionCall ';'
         | 'return' expression ';'
         | 'break' ';'
         ;

controlCmd: ifCmd | whileCmd;

ifCmd: 'if' '(' expression ')' ':' (cmdBlock)? (elseCmd)? 'end';

elseCmd: 'else' ':' (cmdBlock)?;

whileCmd: 'while' '(' expression ')' ':' (cmdBlock)? 'end';

attributionList: attributionCmd (',' attributionCmd)*;

attributionCmd: ID '=' expression;

ioCmd: 'print' '(' expressionList ')'
      | 'scanf' '(' variableList ')'
      ;

expressionList: expression (',' expression)*;

expression: '(' expression ')'
                | '!' expression
                | '-' expression
                | expression ('*'|'/') expression
                | expression ('+'|'-') expression
                | expression ('<'|'>'|'<='|'>=') expression
                | expression ('=='|'!=') expression
                | functionCall
                | literal
                | ID
                ;

functionCall: ID '(' (expressionList)? ')';

variableList: ID | ID ',' variableList;

type: 'int' | 'float' | 'str' | 'bool';
literal: INT | FLOAT | STRING | BOOL;
INT: [0-9]+;
FLOAT: [0-9]+ '.' [0-9]+;
STRING: '"' .*? '"';
BOOL: 'true' | 'false';
ID: [a-zA-Z][a-zA-Z0-9_]*;

OneLineComment: '//' .*? '\n' -> skip;
MultiLineComment: '/*' .*? '*/' -> skip;
WS: [ \t\r\n]+ -> skip;