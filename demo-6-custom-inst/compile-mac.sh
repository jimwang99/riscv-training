#!/bin/bash
## 1st pass: without GCC support
source ~/docker/dev/riscv.sh/rv64i-custom.sh
rm mac.elf
${RISCV}/bin/riscv64-unknown-elf-gcc mac.c -o mac.elf && \
${RISCV}/bin/riscv64-unknown-elf-objdump -d mac.elf > mac-no-gcc.elf.dump
echo "--- elf.dump without gcc support ---"
grep custom0 mac-no-gcc.elf.dump
echo "------------------------------------"

## 2nd pass: with GCC support
source ~/docker/dev/riscv.sh/rv64i-custom-gcc.sh
rm mac.elf
${RISCV}/bin/riscv64-unknown-elf-gcc mac.c -o mac.elf && \
${RISCV}/bin/riscv64-unknown-elf-objdump -d mac.elf > mac-with-gcc.elf.dump

echo "--- elf.dump with gcc support ---"
grep custom0 mac-with-gcc.elf.dump
echo "---------------------------------"
