grammar uciPurdueUnix;


files    : '<' NUMBER '>' ;
utility  : WORD           ;
argument : (TEXT | files) ;
command  : utility OPTIONS argument* ;
pipeline : command (PIPE command)*   ;
session  : SESS_START pipeline* SESS_END ;




NUMBER     : [0-9]+      ;
TEXT       : [A-z]       ;
WORD       : TEXT+       ;
WHITESPACE : (' ' | '\t') -> skip;
SESS_START : '**SOF**'    ;
SESS_END   : '**EOF**'    ;
PIPE       : '|'          ; 
OPTION     : '-' (TEXT)   ;
OPTIONS    : OPTION*      ;
