#include <stdio.h>
#include <stdint.h>

uint32_t byte_matrix_a [4][4] = {
    {42,    212,    87,     145 },
    {20,    172,    57,     135 },
    {37,    211,    135,    206 },
    {108,   180,    187,    46  }
};

uint32_t byte_matrix_b [4][4] = {
    {200,   17 ,    165,    127 },
    {255,   128,    135,    189 },
    {178,   136,    177,    53  },
    {209,   163,    21 ,    175 }
};

int32_t ref_result [4][4] = {
    {108251,    63317,  53994,  75388   },
    {86221 ,    52113,  39444,  61694   },
    {128289,    79575,  62811,  87783   },
    {110400,    57806,  76185,  65697   }
};

int32_t result [4][4] = {
    {0, 0, 0, 0},
    {0, 0, 0, 0},
    {0, 0, 0, 0},
    {0, 0, 0, 0}
};

int main(void) {
    float f, g, h;
    f = 3.2;
    g = 5.6;
    h = f * g;

    int32_t a, b, sum, ref;
    int i, x, y;

    x = 0;
    y = 0;
    ref = ref_result[x][y];

    sum = 0;
    for (i=0; i<4; i++) {
        a = byte_matrix_a[x][i];
        b = byte_matrix_b[i][y];
        sum += a * b;
    }

    if (sum != ref) {
        printf("@FAIL: sum(%d) != ref(%d)\n", sum, ref);
        return 1;
    }

    printf("@PASS\n");
    return 0;
}
