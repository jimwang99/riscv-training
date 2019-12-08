#!/bin/bash
source ~/docker/dev/riscv.sh/rv64i-custom.sh
rm test.elf test.elf.dump
${RISCV}/bin/riscv64-unknown-elf-gcc test.c -o test.elf && \
${RISCV}/bin/riscv64-unknown-elf-objdump -D test.elf > test.elf.dump
grep custom0 test.elf.dump
