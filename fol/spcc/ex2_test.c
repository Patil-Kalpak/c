int main()
{
    int a = 10;
    float b = 5.5;

    if(a > 5 && b < 10)
    {
        a = a + 1;
    }

    return 0;
}


// commands to run
// flex odd.l
// gcc lex.yy.c
// ./a.out < test.c