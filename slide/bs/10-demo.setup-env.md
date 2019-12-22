title: @DEMO: Setup lab environment
class: animation-fade
layout: true

<!-- This slide will serve as the base layout for all your slides -->

.bottom-bar[
RISC-V Architecture Training - Created by Jim Wang (http://phdbreak99.github.io) - Dec. 2019 - All rights Reserved
]

---

class: impact

## RISC-V ARCHITECTURE TRAINING

&nbsp;

# @DEMO: Setup lab environment

&nbsp;

Jim Wang (http://phdbreak99.github.io)

Dec. 2019


---

## Install VMWare Player

---

## Create Ubuntu 16.04 from provided virtual machine

```
Username = riscv
Password = r5rocks
```

---

## Install Freedom Studio from SiFive

```
https://www.sifive.com/boards
```

They have Windows / Mac OS / Linux versions.

### @LAB

Path in LAB VM

```
/opt/FreedomStudio-2019-08-2-lin64
```

---

## Setup shell environment

```
export SIFIVE=/opt/FreedomStudio-2019-08-2-lin64/SiFive
export RISCV=${SIFIVE}/riscv64-unknown-elf-gcc-8.3.0-2019.08.0
export QEMU=${SIFIVE}/riscv-qemu-4.1.0-2019.08.0

export PATH=${RISCV}/bin:${QEMU}/bin:${PATH}
```

### @LAB

Above setup has been added into .bashrc

---

## @LAB: Hello world

```
cd ~/riscv-training/lab/20-lab.setup-env
make
```

Here is the log:

```
make hello.elf SRC_TYPE=c
make[1]: Entering directory '/mnt/hgfs/riscv-training/lab/20-lab.setup-env'
/opt/FreedomStudio-2019-08-2-lin64/SiFive//riscv64-unknown-elf-gcc-8.3.0-2019.08.0/bin/riscv64-unknown-elf-gcc hello.c -o hello.elf
make[1]: Leaving directory '/mnt/hgfs/riscv-training/lab/20-lab.setup-env'
make hello.spike.log
make[1]: Entering directory '/mnt/hgfs/riscv-training/lab/20-lab.setup-env'
/opt/FreedomStudio-2019-08-2-lin64/SiFive//riscv64-unknown-elf-gcc-8.3.0-2019.08.0/bin/spike /opt/FreedomStudio-2019-08-2-lin64/SiFive//riscv64-unknown-elf-gcc-8.3.0-2019.08.0/riscv64-unknown-elf/bin/pk hello.elf | tee hello.spike.log
bbl loader
*Hello world!
make[1]: Leaving directory '/mnt/hgfs/riscv-training/lab/20-lab.setup-env'
make hello.spike.trace
make[1]: Entering directory '/mnt/hgfs/riscv-training/lab/20-lab.setup-env'
/opt/FreedomStudio-2019-08-2-lin64/SiFive//riscv64-unknown-elf-gcc-8.3.0-2019.08.0/bin/spike -l /opt/FreedomStudio-2019-08-2-lin64/SiFive//riscv64-unknown-elf-gcc-8.3.0-2019.08.0/riscv64-unknown-elf/bin/pk hello.elf >& hello.spike.trace
```

---

class: middle, center

![](./image/thanks.jpg)
