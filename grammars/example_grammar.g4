grammar example_grammar;	

operation  : NUMBER '+' NUMBER ; 
NUMBER     : [0-9]+ ;
WHITESPACE : ' ' -> skip ;
