#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <string.h>

int* twoSum(int* nums, int numsSize, int target) {
    
    int* answer = malloc(sizeof(int)*2);
    
    int* sumsides = malloc(sizeof(int)*target+1);
    bzero(sumsides,sizeof(int)*target+1);
    
    int i;
    for(i=0; i<numsSize;){
        //printf("%d,", i);
        if(sumsides[target-nums[i]]){
            answer[0]=sumsides[target-nums[i]];
            answer[1]=++i;
            return answer;
        } else {
            sumsides[nums[i]]=++i;
        }
    }
    
}

int main(){
    int nums[3] = {3,2,4};

    int* answer = twoSum(nums,3,6);

    printf("%d,%d\n",answer[0],answer[1]);

}