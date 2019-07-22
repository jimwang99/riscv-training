#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>

int static_array [4];

int main(void) {
    // malloc
    int dynamic_array [4];
    int * malloc_array1;
    int * malloc_array2;
    
    printf("static_array address = %llx\n", static_array);
    printf("dynamic_array address = %llx\n", dynamic_array);

    malloc_array1 = (int*) malloc (4);
    printf("malloc_array1 address = %llx\n", malloc_array1);
    free(malloc_array1);

    malloc_array2 = (int*) malloc (4);
    printf("malloc_array2 address = %llx\n", malloc_array2);
    free(malloc_array2);

    return 0;
}
