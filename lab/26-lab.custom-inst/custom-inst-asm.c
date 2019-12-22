#include <stdio.h>

int main(void) {
    int a, b, c;
    a = 5;
    b = 2;
    c = 0;

    asm volatile
        (
         "custom0.madd.s  %[z], %[a], %[b], %[c]\n\t"
         : [z] "=r" (c)
         : [a] "r" (a), [b] "r" (b), [c] "r" (c)
        );

    if ( c != 10.0 ){
        printf("@FAIL\n");
        return 1;
    }

    printf("@PASS\n");

    return 0;
}
