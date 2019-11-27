#include <stdio.h>

int main(void) {
    FILE *fpi;
    FILE *fpo;
    char str[100];

    fpi = fopen("in.txt", "r");
    fpo = fopen("out.txt", "w");

    while (fgets(str, 100, fpi) != NULL) {
        printf("%s", str);
        fprintf(fpo, "%s", str);
    }
    fclose(fpi);
    fclose(fpo);

    return 0;
}
