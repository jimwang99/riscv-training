# compile
${RISCV}/bin/riscv64-unknown-elf-gcc example-c.c -o example-c.elf
# object dump
${RISCV}/bin/riscv64-unknown-elf-objdump -D example-c.elf > example-c.elf.dump
