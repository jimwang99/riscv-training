#include <stdio.h>

int main(void) {
    printf("before breakpoint\n");
    
    asm volatile
        (
         "ebreak\n\t"
         :
         :
        );

    printf("after breakpoint\n");
    return 0;
}
