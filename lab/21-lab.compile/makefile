default: asm c

asm:
	make example-asm.elf SRC_TYPE=asm
	make example-asm.elf.dump
	make example-asm.spike.log
	#make example-asm.spike.trace
c:
	make example-c.elf SRC_TYPE=c CCOPT="-Ofast"
	make example-c.elf.dump
	make example-c.spike.log
	#make example-c.spike.trace
.PHONY: default asm c

include ../make.setup.in
include ../make.compile.in
include ../make.spike.in
