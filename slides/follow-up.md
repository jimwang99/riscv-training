class: impact
# Follow-up question from yesterday

## 1. What is GP's purpose?

## 2. Software breakpoint

---

## GP (global pointer) register

### GP is a pointer to global variables

GP is pointing at the center of `.data` section that allows program to index to any global variables easily without the need to `auipc` every time

### Example: C program uses global variables

```C
/* Global Variables: */
Boolean         Bool_Glob;
char            Ch_1_Glob,
                Ch_2_Glob;
Proc_4 () /* without parameters */ {
  Boolean Bool_Loc;
  Bool_Loc = Ch_1_Glob == 'A';
  Bool_Glob = Bool_Loc | Bool_Glob;
  Ch_2_Glob = 'B';
} /* Proc_4 */
```

---

## GP (global pointer) register (cont'd)

### ASM disabled GP

```assembly
0000000040400826 <Proc_4>:
    40400826:   3fc00797                auipc   a5,0x3fc00
    4040082a:   f777c783                lbu     a5,-137(a5) # 8000079d <Ch_1_Glob>
    4040082e:   3fc00717                auipc   a4,0x3fc00
    40400832:   f7272703                lw      a4,-142(a4) # 800007a0 <Bool_Glob>
    40400836:   fbf78793                addi    a5,a5,-65
    4040083a:   0017b793                seqz    a5,a5
    4040083e:   8fd9                    or      a5,a5,a4
    40400840:   3fc00717                auipc   a4,0x3fc00
    40400844:   f6f72023                sw      a5,-160(a4) # 800007a0 <Bool_Glob>
    40400848:   3fc00797                auipc   a5,0x3fc00
    4040084c:   04200713                li      a4,66
    40400850:   f4e78a23                sb      a4,-172(a5) # 8000079c <Ch_2_Glob>
    40400854:   8082                    ret
```

---

## GP (global pointer) register (cont'd)

### ASM enabled GP

```c
00000000400003f0 <Proc_4>:
    400003f0:   8651c783                lbu     a5,-1947(gp) # 80001fbd <Ch_1_Glob>
    400003f4:   8681a703                lw      a4,-1944(gp) # 80001fc0 <Bool_Glob>
    400003f8:   fbf78793                addi    a5,a5,-65
    400003fc:   0017b793                seqz    a5,a5
    40000400:   00e7e7b3                or      a5,a5,a4
    40000404:   86f1a423                sw      a5,-1944(gp) # 80001fc0 <Bool_Glob>
    40000408:   04200713                li      a4,66
    4000040c:   86e18223                sb      a4,-1948(gp) # 80001fbc <Ch_2_Glob>
    40000410:   00008067                ret
```

---

## GP (global pointer) register (cont'd)

### TP (thread pointer) is a pointer to thread-level global variables (aka thread-local storage)

---

## Software breakpoint and `EBREAK` instruction

- Breakpoint is always used for software debug.
- `EBREAK` instruction will trigger a breakpoint exception, and trap into trap handler. Then kernel will decided what to do after that.	

### What does PK do?

#### Example C code

```c
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
```

---

## Software breakpoint and `EBREAK` instruction

Print out breakpoint info and return.

```assembly
> spike pk bp.elf
bbl loader
before breakpoint
z  0000000000000000 ra 00000000000101c0 sp 000000007f7e9b40 gp 0000000000013f48
tp 0000000000000000 t0 8801000500000001 t1 0000000000000007 t2 0000219000040077
s0 000000007f7e9b50 s1 0000000000000000 a0 000000000000000a a1 0000000000014760
a2 0000000000000012 a3 0000000000000000 a4 0000000000000000 a5 0000000000000001
a6 000000000000000a a7 0000000000000040 s2 0000000000000000 s3 0000000000000000
s4 0000000000000000 s5 0000000000000000 s6 0000000000000000 s7 0000000000000000
s8 0000000000000000 s9 0000000000000000 sA 0000000000000000 sB 0000000000000000
t3 0000000000000000 t4 000000005d3724c0 t5 0000000000000000 t6 0000000000000000
pc 00000000000101c0 va 00000000000101c0 insn       ffffffff sr 8000000200046020
Breakpoint!
z  0000000000000000 ra 0000000000010362 sp 000000007f7e9ad0 gp 0000000000013f48
tp 0000000000000000 t0 8801000500000001 t1 0000000000000007 t2 0000219000040077
s0 0000000000013728 s1 00000000000006e9 a0 00000000000006e9 a1 00000000000006e9
a2 0000000000000012 a3 0000000000000000 a4 00000000000006e9 a5 0000000000000001
a6 000000000000000a a7 0000000000000040 s2 0000000000000000 s3 0000000000000000
s4 0000000000000000 s5 0000000000000000 s6 0000000000000000 s7 0000000000000000
s8 0000000000000000 s9 0000000000000000 sA 0000000000000000 sB 0000000000000000
t3 0000000000000000 t4 000000005d3724c0 t5 0000000000000000 t6 0000000000000000
pc 0000000000010438 va 00000000000006e9 insn       ffffffff sr 8000000200046020
User load segfault @ 0x00000000000006e9
```
---

## Software breakpoint and `EBREAK` instruction

#### Problem `User load segfault`

-   Demo the process of debugging this problem

-   Cause: `ebreak` is a 16-bit instruction, but the breakpoint handler used `mepc += 4` before `sret` that skipped one necessary 16-bit instruction.
    -   If it's a 32-bit instruction, it will cause `illegal_instruction` exception immediately

#### After apply `.option norvc`

```assembly
> spike -m16 pk bp_norvc.elf
bbl loader
before breakpoint
z  0000000000000000 ra 00000000000101c0 sp 0000000000fd9b40 gp 0000000000013f58
tp 0000000000000000 t0 8800000503e80001 t1 0000000000000007 t2 000021900003000e
s0 0000000000fd9b50 s1 0000000000000000 a0 000000000000000a a1 0000000000014770
a2 0000000000000012 a3 0000000000000000 a4 0000000000000000 a5 0000000000000001
a6 000000000000000a a7 0000000000000040 s2 0000000000000000 s3 0000000000000000
s4 0000000000000000 s5 0000000000000000 s6 0000000000000000 s7 0000000000000000
s8 0000000000000000 s9 0000000000000000 sA 0000000000000000 sB 0000000000000000
t3 0000000000000000 t4 000000005d378e40 t5 0000000000000000 t6 0000000000000000
pc 00000000000101c0 va 00000000000101c0 insn       ffffffff sr 8000000200046020
Breakpoint!
after breakpoint
```

---

# Welcome to my blog 
### http://phdbreak99.github.io

&nbsp;

# Training material

### http://phdbreak99.github.io/riscv-training/list.html

### http://github.com/phdbreak99/riscv-training

&nbsp;

# Welcome to connect me on LinkedIn

### https://www.linkedin.com/in/wangjun99



