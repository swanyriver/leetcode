#include <stdio.h>
#include <stdlib.h>
#include <string.h>

const int width = 100;
double widthunit;

struct pointpair{
    double start;
    double end;
};

typedef struct pointpair drop;
typedef struct pointpair wetspot;

drop getRaindrop() {

    drop output;

    float length = rand()%3 + 1;
    output.start = (long double) rand() / widthunit;
    output.start -= length/2;
    output.end = output.start+length;

    return output;
}

int main(int argc, char const *argv[])
{
    widthunit = (long double) RAND_MAX/width;
    

    struct wetList
    {
        wetspot wetpoint;
        wetList* next=NULL;
    };



    wetList first;
    wetList.wetpoint = getRaindrop();

    int numDrops = 1;
    drop mydrop;
    wetList* cursor = &first;

    while (  ! ( first.wetpoint.start <= 0 && first.wetpoint.end >= width )  ){
        mydrop = getRaindrop();
        ++numDrops;

        cursor = &first;


        while (mydrop.start < cursor)

    }

    printf("%d drops\n", numDrops);
}

