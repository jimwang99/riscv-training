{{ title_page('Demo 6: Create custom instructions') }}

---

{{ toc_page('Custom instruction', 'Instruction encoding', 'binutils', 'SPIKE', 'GCC') }}

---

{{ toc() }}

---

## Custom instruction

### The most attractive feature for RISC-V

- Extensibility
- Differentiation
- Software hardware co-design
    - Domain-specific applications

&nbsp;

- Example
    - Integer MAC (multiplication and accumulation) for matrix operation
    - Multiple load/store fusion for smaller code footprint
    - Customized vector operations tailored for your application

---

## Custom instruction / difficulties

### Not in hardware, but in compiler

- How to let compiler understand your intention and generate corresponding instructions
- For example, automatic vectorization is difficult with vector/SIMD instructions
    - The compiler has to understand the `for` loop, as well as the implemention details

---

## Example: new MAC instruction

### MAC = multiplication and accumulation
-   `c += a * b` (`RD = RD + RS1 * RS2`)
-   Most common operations in matrix multiplication

### How to handle Overflow?

-   Use separate instructions to read out higher/lower parts
    -   Just like `mul` and `mulh`
-   Use implicitly defined register pair to store result.
    -   If `RD == t0`, then `{t0, t1} = {t0, t1} + RS1 * RS2`
-   Use implicit dedicated register to store result
    -   Need extra command to move in/out of this implicit dedicate register
-   Simple ignore overflow bits, just other mechanism to detect overflow
    -   Just like `add` and `sub`
    -   Choose this approach in this demo

---

{{ toc() }}

---

## Example / select instruction encoding

### Which format?

![:scale 80%](image/instruction-formats.png)

-   Type R: because we need all `rd`, `rs1` and `rs2` while no immediate number

---

## Example / select instruction encoding

### Which opcode?

![:scale 80%](image/opcode-map.png)

-   We can use custom-0: `inst[6:2] = 0b00010 = 0x02` while `inst[1:0] = 0b11` as always for 32-bit instruction

-   `funct3 = 0b000` and `funct7 = 0b0000000`

---

## Example / GNU toolchain support

### Hardware support?

Obviously needed

### Software support? (How to use new instruction?)

1. Write binary code directly
    - Very hard to use/debug
    - Quick and dirty
2. Write embedded assembly code (GNU toolchain: binutils)
    - Easier to use, manual/full control
    - Still not very obvious
3. Compiler automatically pickup the routine (GNU toolchain: GCC)
    - Easy to use but hard to control
    - Compiler is not that intelligent

---

{{ toc() }}

---

## Example / binutils

### 1. Generate opcodes

```shell
> cd ~/docker/riscv/riscv-tools/riscv-opcodes
```

Add the following line to `opcodes.custom`
```
# R-type
custom0.madd.s    rd rs1 rs2 rs3    26..25=0 14..12=0 6..2=0x02 1..0=3
```

Generate opcode:
```shell
> cat opcodes-custom | ./parse-opcodes -c | grep CUSTOM0
#define MATCH_CUSTOM0_MADD_S 0xb
#define MASK_CUSTOM0_MADD_S  0x600707f
DECLARE_INSN(custom0_madd_s, MATCH_CUSTOM0_MADD_S, MASK_CUSTOM0_MADD_S)
```

---

## Example / binutils

### 2. Add opcode to binutils

- Add previously generated opcode lines to `~/docker/riscv/riscv-gnu-toolchain/riscv-binutils/include/opcode/riscv-opc.h`

- Add the following line to `const struct riscv_opcode riscv_opcodes[]` in `~/docker/riscv/riscv-gnu-toolchain/riscv-binutils/opcodes/riscv-opc.c`
```cpp
{"custom0.madd.s", 0, {"I", 0}, "d,s,t,r",  MATCH_CUSTOM0_MADD_S, MASK_CUSTOM0_MADD_S, match_opcode, 0 },
```
Here lower case `d,s,t,r` means GPR registers as destination, source, target, register3.

.footnote[This is the only integer instruction that has 4 operands: 3 inputs and 1 output]

---

## Example / binutils

### 2. Add opcode to binutils

- Add support for `'r'` in `print_insn_args` in file `~/docker/riscv/riscv-gnu-toolchain/riscv-binutils/opcodes/riscv-dis.c`
```cpp
for (; *d != '\0'; d++) {
    switch (*d) {
    ...
        case 'r':
            print (info->stream, "%s", riscv_gpr_names[EXTRACT_OPERAND (RS3, l)]);
            break;
     ...
```

---

## Example / binutils

### recompile gnu-toolchain

```shell
> cd ~/docker/riscv/riscv-gnu-toolchain; mkdir build-rv64i-custom-newlib; cd $_
> ../configure --prefix=/opt/riscv/rv64i-custom --with-arch=rv64i --with-abi=lp64
> make -j6 | tee log
```

---

## Try it out: GCC assembler

Source file
`~/docker/riscv/riscv-training/demo-6-custom-inst/test.c`

Script
`~/docker/riscv/riscv-training/demo-6-custom-inst/compile-test.sh`


---

{{ toc() }}

---

## Example / SPIKE

Need to add corresponding custom instruction support in SPIKE as golden reference

### Regenerate `encoding.h`

```shell
cd ~/docker/riscv/riscv-tools/riscv-opcodes
cp encoding.h new-encoding.h
cat opcodes opcodes-rvc-pseudo opcodes-rvc opcodes-custom | ./parse-opcodes -c >> new-encoding.h

# this time we can use the whole file
cp new-encoding.h ~/docker/riscv/riscv-tools/riscv-isa-sim/riscv/encoding.h
cp new-encoding.h ~/docker/riscv/riscv-tools/riscv-isa-sim/fesvr/encoding.h
```

---

## Example / SPIKE

### New instruction heading file

Create instruction behavior heading file for new MAC instruction

`~/docker/riscv/riscv-tools/riscv-isa-sim/riscv/insns/custom0_madd_s.h`

{{ include_code('~/docker/riscv/riscv-tools/riscv-isa-sim/riscv/insns/custom0_madd_s.h', 'c'))

To support using `RS3` as the 3rd source register, we need to change `~/docker/riscv/riscv-tools/riscv-isa-sim/riscv/decode.h`

```c
#define RS1 READ_REG(insn.rs1())
#define RS2 READ_REG(insn.rs2())
#define RS3 READ_REG(insn.rs3())
```

---

## Example / SPIKE

### Add new instruction to `riscv_insn_list` inside file:

`~/docker/riscv/riscv-tools/riscv-isa-sim/riscv/riscv.mk.in`

---

## Example / SPIKE

### Add to SPIKE disassember

So that it can be correctly disassemble new instruction

`~/docker/riscv/riscv-tools/riscv-isa-sim/spike_main/disasm.cc`

```c
// new xrs3 argument to support 3rd source register in MAC
struct : public arg_t {
  std::string to_string(insn_t insn) const {
    return xpr_name[insn.rs3()];
  }
} xrs3;

disassembler_t::disassembler_t(int xlen)
{
    ...
    #define DEFINE_RTYPE(code) DISASM_INSN(#code, code, 0, {&xrd, &xrs1, &xrs2})
    // to support 3rd source register
    #define DEFINE_R3TYPE(code) DISASM_INSN(#code, code, 0, {&xrd, &xrs1, &xrs2, &xrs3})
    ...
    DEFINE_RTYPE(add);
    DEFINE_R3TYPE(custom0_madd_s); // MAC
    ...
}
```

---

## Example / SPIKE

### Compile SPIKE
```shell
cd ~/docker/riscv/riscv-tools
source ~/docker/dev/riscv.sh/rv64i-custom.sh
./build-spike-only.sh
```

---

{{ toc() }}

---

## Example / GCC

Only use assembly is not enough, we need GCC to automatically generate new instruction from C code

### Define new instruction

`~/docker/riscv/riscv-gnu-toolchain/riscv-gcc/gcc/config/riscv/riscv.md`

```
;; custom0.madd.s
(define_insn "fmasi4"
  [(set (match_operand:SI             0 "register_operand" "=r")
        (fma:SI   (match_operand:SI   1 "register_operand" " r")
                  (match_operand:SI   2 "register_operand" " r")
                  (match_operand:SI   3 "register_operand" " r")))]
  "TARGET_64BIT"
  "custom0.madd.s\t%0,%1,%2,%3"
  [(set_attr "type" "imadd")
   (set_attr "mode" "SI")]
)
```

---

## Example / GCC

### Define new instruction

- `fmasi4` is the standard function name
    - `fma` = multiply add fusion
    - `si` is the *mode* (in the doc, it's abbreviated as *m*). `si` means full-word integer
    - `4` means 4 operands, 3 on the right hand side, 1 on the left
    - More definition can be found at https://gcc.gnu.org/onlinedocs/gccint/Standard-Names.html
- `custom0.madd.s\t%0,%1,%2,%3` is the abstraction of assembly code

Reference at [Introduction to Machine Description](./pdf/Introduction-to-Machine-Description-in-GCC.pdf)

---

## Example / GCC

### Recompile GCC

```
> cd ~/docker/riscv/riscv-gnu-toolchain; mkdir build-rv64i-custom-newlib; cd $_
> ../configure --prefix=/opt/riscv/rv64i-custom --with-arch=rv64i --with-abi=lp64
> make -j6 | tee log
```

---

## Try it out: GCC support


Source file
`~/docker/riscv/riscv-training/demo-6-custom-inst/mac.c`

Script
`~/docker/riscv/riscv-training/demo-6-custom-inst/compile-mac.sh`

---

{{ thanks() }}

---

class: middle, center

## DIY: custom instruction

### Create custom instruction to implement Sigmoid

$$S(x)=1/(1+e^{-x})=e/(e^x+1)$$
