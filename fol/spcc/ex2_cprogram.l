%{
#include<stdio.h>
%}

digit      [0-9]
id         [a-zA-Z_][a-zA-Z0-9_]*
floatnum   {digit}+"."{digit}+

%%

"int"|"float"|"char"|"if"|"else"|"while"|"for"|"return"
        { printf("Keyword : %s\n",yytext); }

{id}    { printf("Identifier : %s\n",yytext); }

{floatnum}
        { printf("Float : %s\n",yytext); }

{digit}+
        { printf("Integer : %s\n",yytext); }

"+"|"-"|"*"|"/"|"%"
        { printf("Arithmetic Operator : %s\n",yytext); }

"&&"|"||"|"!"
        { printf("Logical Operator : %s\n",yytext); }

"=="|"!="|">"|"<"|">="|"<="
        { printf("Relational Operator : %s\n",yytext); }

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