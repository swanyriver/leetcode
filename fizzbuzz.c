#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char const *argv[])
{

    int fizz = 3;
    int buzz = 5;

    for (int i = 1; i <= 100; ++i)
    {
        --fizz;
        --buzz;
        if(fizz && buzz){
            printf("%d\n", i);
        }else{
            if(!fizz){
                printf("%s","Fizz");
                fizz=3;
            }
            if(!buzz){
                printf("%s", "buzz" );
                buzz=5;
            }
            putchar('\n');
        }
    }
    return 0;
}