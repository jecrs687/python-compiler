grammar trab;
prog: decVars* decFuncoes* blocoMain;
listaDecVars returns [int value]: listaIds|listaAtribs ;
decVars returns [int value]: tipo (listaDecVars)';';
decParam returns [int value]: tipo (ID);
tipo returns [int value]
:'int'
|'float'
|'boolean'
|'string'
;
listaIds returns [int value]: ID (',' ID)*;
atrib returns [int value]: ID '=' (expr);
listaAtribs returns [int value]: atrib (',' atrib)*;
tipoFunc returns [int value]: tipo | 'void';
decFuncoes returns [int value]: 'def' tipoFunc ID '('(decParam (',' decParam)*)?')' ':' stmts* '}' # DecFunc
;
returnFunc returns [int value]: 'return' expr ';';
blocoMain returns [int value]: 'main' '(' ')' ':' stmts* '}';
stmts returns [int value]
: cmdAtrib
| cmdIf
| cmdFor
| cmdWhile
| printFunc
| inputFunc ';'
| callFunction ';'
| returnFunc
;
stmts_break returns [int value]: stmts | cmdIf_break  | 'break' ';'
;
callFunction returns [int value]: ID '('(expr (',' expr)*)?')';
cmdAtrib returns [int value]: ID '=' expr ';';
elseIf returns [int value]: 'else' ':' stmts* '}';
normalIf returns [int value]: 'if' expr ':' stmts* '}';
cmdIf returns [int value]: normalIf (elseIf)? # IfCond
;
cmdIf_break returns [int value]: 'if' expr ':' stmts_break* '}' ('else' ':' stmts_break* '}')? # IfBreakCond
;
cmdFor returns [int value]: 'for' ID 'in' 'range' '('e1=(INT|ID) ',' e2=(INT|ID)')' ':' stmts_break* '}' # ForCond
;
cmdWhile returns [int value]: 'while' (expr) ':' stmts_break*'}' # WhileCond
;
printExpr returns [int value]: expr
;
printSec returns [int value]: ',' (printExpr)
;
printFunc returns [int value]: 'print' (printExpr) printSec* ';';
inputFunc returns [int value]: ID '=' 'input' '(' ')';

expr returns [int value]
    :
    callFunction                                                    # CallExpr
    | '-'+ e=expr                                                   # MinusExpr
    | '+'+ e=expr                                                   # PlusExpr
    | 'not' + e=expr                                                  # NegateExpr
    | e1=expr op=('*' | '/')+ e2=expr                               # MulDivExpr
    | e1=expr op=('+' | '-')  e2=expr                               # AddSubExpr
    | e1=expr op=('>' | '<' | '>=' | '<=')+ e2=expr                 # CompExpr
    | e1=expr op=('==' | '!=')+ e2=expr                             # CompAllExpr
    | e1=expr op=('and'|'or')+ e2=expr                              # BoolExpr
    | e1=ID                                                         # IdExpr
    | e1=INT                                                        # IntegerExpr
    | e1=FLOAT                                                      # FloatExpr
    | e1=BOOL                                                       # BoolTFExpr
    | e1=STRING                                                     # StringExpr
    | e1='(' expr ')'                                               # ParensExpr
    | e1=cmdAtrib                                                   # AssignExpr
    ;
BOOL: 'True'|'False';
ID: [a-zA-Z][a-zA-Z0-9_]*;
INT: [0-9]+;
STRING: '"' .*? '"';
WS: [ \t\n\r]+-> skip ;
SL_COMMENT: '//' .*? '\n'-> skip ;
FLOAT: [0-9]+('.' [0-9]*);