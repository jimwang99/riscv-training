{{ title_page('Demo 2: PK (proxy kernel) and FESVR (front-end server)') }}

---

{{ toc_page('PK and FESVR') }}

---

{{ toc() }}

---

## PK and FESVRV

-   PK (proxy kernel) & FESVR (front-end server)
    -   For debug and system bring up
    -   PK is an abstraction of kernel that provides system services through FESVR running on host

![:scale 80%](image/riscv-pk-fesvr.png)

---

## PK and FESVR (cont'd)

-   PK is running on target CPU, while FESVR is running on host computer

![:scale 70%](image/fesvr-diagram.png)

---

## PK and FESVR / code example

### `printf`

```shell
> /opt/riscv/rv64gc/bin/spike /opt/riscv/rv64gc/riscv64-unknown-elf/bin/pk hello.elf | tee hello.log
bbl loader
fesvr::sys_getmainvars (0x 8000d860 200 0 0 0 0 0)
fesvr::sys_openat (0x ffffffffffffff9c 8000d8b5 a 0 0 0 0)
fesvr::sys_pread (0x 3 8000d600 40 0 0 0 0)
...
fesvr::sys_pread (0x 3 80830000 1000 a000 0 0 0)
fesvr::sys_fstat (0x 1 80024df0 0 0 0 0 0)
fesvr::sys_pread (0x 3 8082c000 1000 6000 0 0 0)
fesvr::sys_write (0x 1 80834230 d 0 0 0 0)
Hello world!
fesvr::sys_exit (0x 0 0 0 0 0 0 0)
```

---

## PK and FESVR / system call

.col-6[

### `tohost` and `fromhost`

-   Memory location: shared knowledge between PK and FESVR
-   Both are 32-bit size, that can be read/write with single access
-   Follow producer-consumer model
    -   `tohost` is written by PK, cleared by FESVR
    -   `fromhost` is written by FESVR, cleared by PK

]

.col-6[

### `magicmem`

-   `tohost` and `fromhost` are too small to communicate real data structure. They only store the address of `magicmem`
-   Syscall type, arguments and return values are stored in `magicmem`

]

.col-12[

### Syscall entry point in PK

`~/docker/riscv/riscv-tools/riscv-pk/pk/syscall.c`

### Syscall handler in FESVR

`~/docker/riscv/riscv-tools/riscv-isa-sim/fesvr/syscall.cc`

]

---

## PK and FESVR / system call workflow

> Please remember, this is for debugging hardware and system bring-up, sometimes co-processor running enviroment. And it's good for understanding application/kernel interaction.

| Target side (PK on RISC-V)                    | Host side (FESVR on x86)                                 |
| --------------------------------------------- | -------------------------------------------------------- |
| User-level code: `ecall` and trap into PK     |                                                          |
| Write syscall arguments into **magicmem**     |                                                          |
| Write address of **magicmem** into **tohost** | Looping: read **tohost** until it's non-0                |
|                                               | Read **magicmem**                                        |
| Looping: read **tohost** until it's 0         | Write 0 to **tohost**                                    |
|                                               | Deal with syscall. Write return values into **magicmem** |
| Looping: read **fromhost** until it's non-0   | Write address of **magicmem** into **fromhost**          |
| Read **magicmem**                             |                                                          |
| Write 0 to **fromhost**                       | Looping: read **fromhost** until it's 0                  |



---

## PK and FESVR / verification exit

### Another very useful scenario

- To pass exit code in verification. It's embedded inside the `riscv-tests` verification suite.
- `RVTEST_PASS` and `RVTEST_FAIL` in `~/docker/riscv/riscv-tools/riscv-tests/env/p/riscv_test.h`

---

{{ thanks() }}

---

class: middle, center

## DIY: new system call

### Add new system call to synchronize system time between target and host

Read CSR of `mtime` to get system time on RISC-V CPU

Need to use assembly code sometime
