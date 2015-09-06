#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int trap(int* height, int heightSize) {
    int currentindex = 0;
    int trappedwater = 0;
    int currentpool = 0;
    int leftEdge
    int leftEdgeIndex = 0;

   

    while(currentindex<heightSize){
        while( ++currentindex < heightSize && height[currentindex] >= height[currentindex-1]);
        leftEdge = height[currentindex-1];
        leftEdgeIndex = currentindex-1;

        for(;currentindex<heightSize && height[currentindex] < leftEdge; ++currentindex){
            currentpool += leftEdge-height[currentindex];
        }
        if(currentindex < heightSize)trappedwater += currentpool;
        currentpool =0;
    }

    --currentindex;

    while(currentindex>leftEdgeIndex){
        while( --currentindex > leftEdgeIndex && height[currentindex] >= height[currentindex+1]);
        leftEdge = height[currentindex+1];

        for(;currentindex > leftEdgeIndex && height[currentindex] < leftEdge; --currentindex){
            currentpool += leftEdge-height[currentindex];
        }
        trappedwater += currentpool;
        currentpool =0;
    }

    return trappedwater;
}

int main(int argc, char const *argv[])
{
    
    int nums[] = {0,0,4,5,2,  1,0,3,8,0, 6};

    printf("%d\n", trap(nums, 11) );


    return 0;
}