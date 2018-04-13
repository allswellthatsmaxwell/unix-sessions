/* Parser rules */

*/ Lexer rules */
WHITESPACE : ' ' -> skip ;
NUMBER     : [0-9]+ ;
TEXT       : [A-z] ;
OPTION     : '-'[NUMBER|TEXT]
FILES      : '<'NUMBER'>'