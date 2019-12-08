# compile
${RISCV}/bin/riscv64-unknown-elf-gcc -nostdlib -nostartfiles example-c.c -o example-c-nostart.o
# link
${RISCV}/bin/riscv64-unknown-elf-ld -T linker-c-nostart.ld example-c-nostart.o -o example-c-nostart.elf
# object dump
${RISCV}/bin/riscv64-unknown-elf-objdump -D example-c-nostart.elf > example-c-nostart.elf.dump

