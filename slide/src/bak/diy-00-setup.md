{{ title_page('DIY 0: Setup DIY environment') }}

---

## Build from scratch vs. pre-compiled toolchain

-   Because RISC-V spec is very scalable
    -   Every systems are different from each other
    -   Most compatible OS: Linux
        -   **Ubuntu 16.04** or CentOS 6 (recently added support)
-   Pre-compiled toolchain (from SiFive)
    -   `riscv64-unknown-elf-gcc-8.2.0-2019.05.3-x86_64-linux-ubuntu14.tar.gz`
        -   Linux Ubuntu version
    -   `riscv64-unknown-elf-gcc-8.2.0-2019.05.3-x86_64-w64-mingw32.zip`
        -   Windows version

---

## Virtual environment

### Choices

-   Docker
    -   Light, flexible
    -   Personally preferred
-   Virtual machine

---

## Virtual environment: docker container

.col-6[
### Docker vs. virtual machine

![:scale 100%](image/docker-vm-container.png)
]

.col-6[
### System Requirements:

- Windows 10 64bit: Pro, Enterprise or Education (Build 15063 or later).
- Virtualization is enabled in BIOS. Typically, virtualization is enabled by default. This is different from having Hyper-V enabled. For more detail see Virtualization must be enabled in Troubleshooting.
- CPU SLAT-capable feature.
- At least 4GB of RAM.
]

---

## Virtual environment: VirtualBox (virtual machine)

### Install VirtualBox

`VirtualBox-6.0.10-132072-Win.exe` is included in the package

### Create VM using provided ubuntu1605.vdi

![:scale 70%](image/virtualbox-install-screenshot.png)

---

## Virtual environment: VirtualBox (virtual machine) (cont'd)

### Inside the VM

#### `/opt/riscv/rv64gc`

Toolchain for 64-bit RISC-V IMAFDC (GC) instruction subsets

#### `~/download/*.tgz`

Pre-downloaded github repositories

| Repository              | Comment              |
| ----------------------- | -------------------- |
| riscv-gnu-toolchain.tgz | GNU toolchain        |
| riscv-tools.tgz         | SPIKE, PK, tests     |
| rocket-chip.tgz         | RocketChip generator |
| qemu.tgz                | QEMU for RISC-V      |
| freedom-u-sdk.tgz       | Precompiled SDK      |

---

{{ thanks() }}
