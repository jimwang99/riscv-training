SHELL=/bin/bash


default:
	@echo "make asm-wrong"
	@echo "make asm-correct"
	@echo "make gcc-wrong"
	@echo "make gcc-correct"

asm-wrong:
	make custom-inst-asm RISCV=/opt/FreedomStudio-2019-08-2-lin64/SiFive/riscv64-unknown-elf-gcc-8.3.0-2019.08.0
	-mkdir wrong
	mv custom-inst-asm.elf wrong
	mv custom-inst-asm.elf.dump wrong
	mv custom-inst-asm.spike.log wrong

asm-correct:
	make custom-inst-asm RISCV=/opt/riscv/rv64i-custom
	-mkdir correct
	mv custom-inst-asm.elf correct
	mv custom-inst-asm.elf.dump correct
	mv custom-inst-asm.spike.log correct

gcc-wrong:
	make custom-inst-gcc RISCV=/opt/FreedomStudio-2019-08-2-lin64/SiFive/riscv64-unknown-elf-gcc-8.3.0-2019.08.0
	-mkdir wrong
	mv custom-inst-gcc.elf wrong
	mv custom-inst-gcc.elf.dump wrong
	mv custom-inst-gcc.spike.log wrong

gcc-correct:
	make custom-inst-gcc RISCV=/opt/riscv/rv64i-custom
	-mkdir correct
	mv custom-inst-gcc.elf correct
	mv custom-inst-gcc.elf.dump correct
	mv custom-inst-gcc.spike.log correct

custom-inst-asm:
	make custom-inst-asm.elf SRC_TYPE=c
	make custom-inst-asm.elf.dump
	make custom-inst-asm.spike.log

custom-inst-gcc:
	make custom-inst-gcc.elf SRC_TYPE=c
	make custom-inst-gcc.elf.dump
	make custom-inst-gcc.spike.log

include ../make.setup.in
include ../make.compile.in
include ../make.spike.in
