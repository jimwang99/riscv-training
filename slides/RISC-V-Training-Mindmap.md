RISC-V Training
	Day 1
		Morning 9:00 - 12:00
			Schedule (15 mins)
			Introduction (1 hour)
			ISA: unprivileged (1.5 hour)
			DIY-0: setup env (0.5 hour)
				docker
				TODO
					download docker for windows
					download virtual-box for windows + ubuntu 16.04 image with X support
		Afternoon 1:30 - 5:30
			Demo-1: baremetal asm & SPIKE simulator (1 hour)
				Debug ASM program use SPIKE
				Example:
			DIY-1: factorial in asm (45 mins)
			tea break
			ISA: privileged (1 hour)
			Demo-2: C code with PK & FESVR (1 hour)
				Compile "Hello World"
					entry.S
					hello.c
					makefile
				System call, from/to host and magic memories
			DIY-2: new system call to sync time (1 hour) (as backup)
				Give some examples that FESVR system time and RISCV system time don't match
				How to get system time in host system?
				How to get/set mtime in RISCV?
	Day 2
		Morning 9:00 - 12:00
			CPU architecture (1 hour)
				Computer architecture basic
					Branch prediction
					pipeline
					multi-issue
					multi-thread
					out-of-order
					memory hierarchy
						cache
						DRAM
				RocketChip
				Boom
				Arian
				Cache coherence
			Demo-3: Verification suite (0.5 hour)
				isa-test
				torture?
				Google's testsuite
			Demo-4: RocketChip generator (1 hour)
				CPU architecture exploration
					Change cache size
				SiFive Core Designer
		Afternoon 1:30 - 5:30
			Demo-5: Freedom IDE & HiFive1 board
				QEMU hello world
				HiFive1 blink LED
			Uncore (1 hour)
				TileLink
				PLIC & CLINT
				Debug
			Demo-6: create custom instruction (1 hour)
			tea break
			DIY-6: create custom instruction (45 mins)
			Demo-7: boot Linux (0.5 hour)
				https://wiki.qemu.org/Documentation/Platforms/RISCV
				uname -a; cat /proc/cpuinfo
				GCC, Python, no GDB
				Compare linux binary with newlib binary
					file size
					run time
			DIY-7: boot Linux on QEMU (0.5 hour)
			Vector extension (1 hour) (as backup)