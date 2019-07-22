SHELL=/bin/bash

################################################################
# compile assembly code
################################################################

bin=/opt/riscv/rv64gc/bin/riscv64-unknown-elf
as=$(bin)-as
ld=$(bin)-ld -T linker-asm.ld
objcopy=$(bin)-objcopy
objdump=$(bin)-objdump
gcc=$(bin)-gcc

compile: $(patsubst %.s,%.elf.dump,$(wildcard *.s)) $(patsubst %.c,%.elf.dump,$(wildcard *.c))
clean:
	-rm *.o *.elf *.bin *.hex *.dump

%.o: %.s
	$(as) $< -o $@

%.elf: %.o
	$(ld) $< -o $@

%.elf.dump: %.elf
	$(objdump) -D $< > $@

%.bin: %.elf
	$(objcopy) -O binary $< $@

%.hex: %.bin
	$(bin2hex) $< > $@

.PRECIOUS: %.elf %.elf.dump


################################################################
# debug with spike
################################################################

spike=spike

log:
	spike -l main.elf 2>&1 | less

it:
	spike -d main.elf

