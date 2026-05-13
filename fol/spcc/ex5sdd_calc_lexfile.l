%{
#include "y.tab.h"
%}

%%

[0-9]+      { yylval = atoi(yytext); return NUM; }

">="        return GE;
"<="        return LE;
"=="        return EQ;
"!="        return NE;

">"         return '>';
"<"         return '<';

"+"         return '+';
"-"         return '-';
"*"         return '*';
"/"         return '/';

"("         return '(';
")"         return ')';

\n          return '\n';

[ \t]       ;

%%

int yywrap()
{
    return 1;
}


