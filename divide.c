#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int divide(int dividend, int divisor) {

    int neg = 0;
    if(dividend < 0 && divisor < 0){
        dividend *=-1;
        divisor *=-1;
    } else if(dividend <0){
        dividend *=-1;
        neg = 1;
    }else if (divisor < 0){
        divisor *=-1;
        neg = 1;
    }

    int i = 0;
    int mask = 1;
    //while(! (dividend & mask ||  divisor & mask ) ){
    while(!  divisor & mask  ){
        mask *=2;
        ++i;
    }
    divisor = divisor >> i;
    dividend = dividend >> i;
    /*while(! (dividend & 1 ||  divisor & 1 ) ){
        divisor = divisor >> 1;
        dividend = dividend >> 1;
        //printf("%d/%d \n", dividend, divisor );
    }*/
    //printf("%d/%d \n", dividend, divisor );

    if (divisor==1) return dividend;

    int answer = 0;
    while(dividend >= divisor){
        dividend-=divisor;
        ++answer;
    }

    if (neg) answer *=-1;

    return answer;
}

int main(int argc, char const *argv[])
{
    if (argc < 3)
    {
        printf("%s\n", "must provided dividend then divisor" );
        return 1;
    }

    int dividend = atoi(argv[1]);

    int divisor = atoi(argv[2]);

    printf("%d/%d = %d \n", dividend, divisor, divide(dividend,divisor) );

    return 0;
}