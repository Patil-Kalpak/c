%{
#include<stdio.h>
%}

id      [a-zA-Z_][a-zA-Z0-9_]*
string  \".*\"

%%

"if"|"else"|"while"|"for"|"def"|"return"|"print"|"import"
        { printf("Keyword : %s\n",yytext); }

{id}
        { printf("Identifier : %s\n",yytext); }

{string}
        { printf("String : %s\n",yytext); }

"+"|"-"|"*"|"/"|"%"
        { printf("Arithmetic Operator : %s\n",yytext); }

"and"|"or"|"not"
        { printf("Logical Operator : %s\n",yytext); }

"=="|"!="|">"|"<"|">="|"<="
        { printf("Relational Operator : %s\n",yytext); }

[0-9]+
        { printf("Number : %s\n",yytext); }

[ \t\n] ;

.       { printf("Special Symbol : %s\n",yytext); }

%%

int yywrap()
{
    return 1;
}

int main()
{
    yylex();
    return 0;
}