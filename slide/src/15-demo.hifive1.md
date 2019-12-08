{{ title_page('Demo 5: Freedom IDE & HiFive1b board') }}

---

{{ toc_page('Freedom IDE', 'Emulate on QEMU', 'Run on HiFive1b board') }}

---

{{ toc() }}

---

## Freedom IDE

![:scale 80%](image/freedom-ide-screenshot.png)

---

## Freedom IDE (cont'd)

### Different targets

.col-7[
| Targets                 | Comments                                          |
| ----------------------- | ------------------------------------------------- |
| qemu-sifive-e31         | QEMU emulator for 32-bit E31 CPU                  |
| qemu-sifive-s51         | QEMU emulator for 64-bit S51 CPU                  |
| freedom-e310-arty       | Arty FPGA platfrom                                |
| sifive-hifive-unleashed | SiFive's HiFive Unleased board that support Linux |
| sifive-hifive1          | SiFive's HiFive1 board                            |
| sifive-hifive1-revb     | SiFive's HiFive1-RevB board                       |
]

.col-5[
![:scale 100%](image/freedom-ide-target.png)
]

---

{{ toc() }}

---

## Emulate on QEMU

-   QEMU is a full system emulator
    -   Translate target instruction to host instruction
    -   Only functional (not trace accurate) but really fast
    -   It's good for software development, not for hardware debugging



### Demo: qemu-sifive-e31-sifive-welcome

```
QEMU emulator version 3.1.0 (SiFive QEMU 3.1.0-2019.05.1)
Copyright (c) 2003-2018 Fabrice Bellard and the QEMU Project developers


                  SIFIVE, INC.

           5555555555555555555555555
          5555                   5555
         5555                     5555
        5555                       5555
       5555       5555555555555555555555
      5555       555555555555555555555555
     5555                             5555
    5555                               5555
   5555                                 5555
  5555555555555555555555555555          55555
   55555           555555555           55555
     55555           55555           55555
       55555           5           55555
         55555                   55555
           55555               55555
             55555           55555
               55555       55555
                 55555   55555
                   555555555
                     55555
                       5


               Welcome to SiFive!

```

---

{{ toc() }}

---

## Run on HiFive1b board

-   HiFive1-revb board
    -   Latest HiFive1 board with FE310

![:scale 60%](image/hifive1b-board.png)


### Demo: sifive-hifive1-revb-sifive-welcome

---

{{ thanks() }}
