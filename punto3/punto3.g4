grammar punto3;

programa
    : expresion EOF
    ;

expresion
    : matriz                          #matrizSola
    | expresion '*' expresion         #multiplicacion
    | '(' expresion ')'               #parentesis
    ;

matriz
    : '[' filas ']'
    ;

filas
    : fila (',' fila)*
    ;

fila
    : '[' elementos ']'
    ;

elementos
    : NUMERO (',' NUMERO)*
    ;

NUMERO
    : '-'? [0-9]+ ('.' [0-9]+)?
    ;

WS
    : [ \t\r\n]+ -> skip
    ;
