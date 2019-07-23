# compile
#${RISCV}/bin/riscv64-unknown-elf-gcc -nostdlib -nostartfiles example-c.c -o example-c.o
${RISCV}/bin/riscv64-unknown-elf-gcc example-c.c -o example-c.o
# link
#${RISCV}/bin/riscv64-unknown-elf-ld -T linker-c.ld example-c.o -o example-c.elf
# object dump
${RISCV}/bin/riscv64-unknown-elf-objdump -D example-c.elf > example-c.elf.dump
