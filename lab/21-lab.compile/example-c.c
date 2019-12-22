#include <stdint.h>
#include <stdio.h>

uint8_t byte_matrix_a [4][4] = {
    {42,    212,    87,     145 },
    {20,    172,    57,     135 },
    {37,    211,    135,    206 },
    {108,   180,    187,    46  }
};

uint8_t byte_matrix_b [4][4] = {
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
    int i, j, k, pass;
    pass = 1;
    for (i=0; i<4; i++) {
        for (j=0; j<4; j++) {
            result[i][j] = 0;
            for (k=0; k<4; k++) {
                result[i][j] += byte_matrix_a[i][k] * byte_matrix_b[k][j];
            }

            if (result[i][j] != ref_result[i][j]) {
                pass = 0;
                // printf("[%d][%d]: result=%d ref=%d\n", i, j, result[i][j], ref_result[i][j]);
            }
        }
    }

    if (pass) {
        return 0;
    } else {
        return 1;
    }
}
