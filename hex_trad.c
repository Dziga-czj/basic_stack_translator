#include <stdlib.h>
#include <stdio.h>

int main(int argc, char* argv[])
{
    if(argc == 1)
    {
        printf("usage : ./hex_trad [hexadecimal string]");
        exit(1);
    }
    
    for (int i = 1; i < argc; i++)
    {
        printf("trad %d : %dx\n", i, argv[i]);
    }
    



    return 0;
}