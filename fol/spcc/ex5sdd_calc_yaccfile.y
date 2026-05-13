%{
#include<stdio.h>
#include<stdlib.h>

int yylex();
void yyerror(char *s);
%}

%token NUM GE LE EQ NE

%%

S : E '\n'     { printf("Result = %d\n",$1); }
  ;

E : E '+' T    { $$ = $1 + $3; }
  | E '-' T    { $$ = $1 - $3; }
  | E '>' E    { $$ = $1 > $3; }
  | E '<' E    { $$ = $1 < $3; }
  | E GE E     { $$ = $1 >= $3; }
  | E LE E     { $$ = $1 <= $3; }
  | E EQ E     { $$ = $1 == $3; }
  | E NE E     { $$ = $1 != $3; }
  | T          { $$ = $1; }
  ;

T : T '*' F    { $$ = $1 * $3; }
  | T '/' F    { $$ = $1 / $3; }
  | F          { $$ = $1; }
  ;

F : '(' E ')'  { $$ = $2; }
  | NUM        { $$ = $1; }
  ;

%%

void yyerror(char *s)
{
    printf("Invalid Expression\n");
}

int main()
{
    printf("Enter Expression : ");
    yyparse();
    return 0;
}

