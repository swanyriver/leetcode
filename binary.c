char* addBinary(char* a, char* b) {
    char* aEnd = a;
    while (*aEnd) ++aEnd;
    
    char* bEnd = b;
    while (*bEnd) ++bEnd;
    
    char carry = '0';
    
    int asize = (aEnd - a) + 1;
    int bsize = (bEnd - b) + 1;
    
    
    char* output;
    if (asize == bsize && *a=='1' && *b=='1') output = malloc(asize+1);
    else output = malloc( (asize>bsize) ? asize : bsize);

    output = output + ((asize>bsize) ? asize : bsize);
    *output = 0;
    int sum;
    
    while(aEnd >= a && bEnd >= b){
        sum = *aEnd-- + *bEnd-- + carry;
        
        --output;
        if(sum == '1'+'1'+'1'){
            *output = '1';
        }
        else if(sum == '1'+'1'+'0'){
            *output = '0';
            carry = '1';
        } else if(sum == '1' + '0' + '0'){
            *output = '1';
            carry = '0';
        } else {
            *output = '0';
        }
    }
    
    char* rem =0;
    char* beg;
    
    if(aEnd > a){
         rem = aEnd;
         beg = a;
    }
    else if(bEnd > b) {
        rem = bEnd;
        beg = b;
    }
    else if(carry == '1'){
        *output = '1';
        return output;
    }else{
        return ++output;
    }
    
    if (carry == '1' && *rem == '1'){
        *output = '0';
        --rem;
    }
    
    while(rem >= beg){
        *--output = *--rem;
    }
    
    
    return output;
}

int main(int argc, char const *argv[])
{
    if (argc < 3) return 1;

    printf("%s\n", addBinary(argv[1],argv[2]) );

    return 0;
}