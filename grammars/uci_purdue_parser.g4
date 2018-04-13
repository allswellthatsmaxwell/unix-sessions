/* Parser rules */

files    : '<' NUMBER '>'
utility  : TEXT+ ;
option   : '-' (TEXT)
argument : (TEXT | FILES)
command  : utility option* argument* ;
pipeline : command (PIPE command)* ;
session  : SESS_START pipeline* SESS_END ;

*/ Lexer rules */
WHITESPACE : ' ' -> skip ;
NUMBER     : [0-9]+ ;
TEXT       : ~ ;
WHITESPACE : (' ' | '\t')
SESS_START : '**SOF**'
SESS_END   : '**EOF**'
PIPE       : '|'