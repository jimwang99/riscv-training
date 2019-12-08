{{ title_page('[20-LAB] Bare-metal assembly & SPIKE simulator') }}

make hello.elf SRC_TYPE=c
make[1]: Entering directory '/mnt/hgfs/riscv-training/lab/20-lab.setup-env'
/opt/FreedomStudio-2019-08-2-lin64/SiFive//riscv64-unknown-elf-gcc-8.3.0-2019.08.0/bin/riscv64-unknown-elf-gcc hello.c -o hello.elf
make[1]: Leaving directory '/mnt/hgfs/riscv-training/lab/20-lab.setup-env'
make hello.spike.log
make[1]: Entering directory '/mnt/hgfs/riscv-training/lab/20-lab.setup-env'
/opt/FreedomStudio-2019-08-2-lin64/SiFive//riscv64-unknown-elf-gcc-8.3.0-2019.08.0/bin/spike /opt/FreedomStudio-2019-08-2-lin64/SiFive//riscv64-unknown-elf-gcc-8.3.0-2019.08.0/riscv64-unknown-elf/bin/pk hello.elf | tee hello.spike.log
bbl loader
Hello world!
make[1]: Leaving directory '/mnt/hgfs/riscv-training/lab/20-lab.setup-env'
make hello.spike.trace
make[1]: Entering directory '/mnt/hgfs/riscv-training/lab/20-lab.setup-env'
/opt/FreedomStudio-2019-08-2-lin64/SiFive//riscv64-unknown-elf-gcc-8.3.0-2019.08.0/bin/spike -l /opt/FreedomStudio-2019-08-2-lin64/SiFive//riscv64-unknown-elf-gcc-8.3.0-2019.08.0/riscv64-unknown-elf/bin/pk hello.elf >& hello.spike.trace
