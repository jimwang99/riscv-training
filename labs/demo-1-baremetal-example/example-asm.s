# filename: ~/docker/training-code/demo-1-baremetal-example.s 
# function: integer matrix multiplication in-memory
.option norvc
.text

.global _start
_start:
li          gp, 0xdeadbeefdeadbeef  # use gp as error flag
j           _main

#===========================================================
# function: multiplication and accummulation
#   a0 = c
#   a1 = a
#   a2 = b
#   a0 = a x b + c
_mac:

mul         t0, a1, a2
add         a0, a0, t0

ret

#===========================================================
# function: vector multiplication
#   a0 = vector length (in byte)
#   a1 = vector a pointer
#   a2 = vector b pointer
#   a0 = return value
_vmul:

# save s* reg to stack, because they are used here
addi        sp, sp, -40
sd          ra, 0(sp)           # push s0
sd          s0, 8(sp)           # push s0
sd          s1, 16(sp)          # push s1
sd          s2, 24(sp)          # push s2
sd          s3, 32(sp)          # push s3
sd          s4, 40(sp)          # push s4

# backup input arguments (a*) to saved reg (s*), because they will be changed for 2nd level function call
mv          s0, a0              # backup vector length to s0
mv          s1, a1              # backup vector a pointer to s1
mv          s2, a2              # backup vector b pointer to s2
mv          s3, a0              # constant vector length saved in s3

mv          a0, x0              # clear a0 to zero (accumulator _mac)

__vmul_mac:
lbu         a1, 0(s1)           # load unsigned byte from vector a
lbu         a2, 0(s2)           # load unsigned byte from vector b
call        _mac                # result in a0
addi        s1, s1, 1           # step vector a pointer
add         s2, s2, s3          # step vector b pointer
addi        s0, s0, -1          # decrease length by 1
bnez        s0, __vmul_mac

# pop s* reg from stack
ld          s4, 40(sp)          # pop s4
ld          s3, 32(sp)          # pop s3
ld          s2, 24(sp)          # pop s2
ld          s1, 16(sp)          # pop s1
ld          s0, 8(sp)           # pop s0
ld          ra, 0(sp)           # pop s0
addi        sp, sp, 40

ret

#===========================================================
_main:                              # main body
la          sp, stack               # initialize stack pointer

ld          s3, byte_matrix_row     # size constant
ld          s4, byte_matrix_col     # size constant

li          s0, 0                   # result index
li          s1, 0                   # row index
li          s2, 0                   # column index

__mmul_row:

__mmul_col:
mv          a0, s4                  # vector length = column #
la          a1, byte_matrix_a
la          a2, byte_matrix_b
mul         t0, s1, s4
add         a1, a1, t0
add         a2, a2, s2
call        _vmul                   # return value in a0

_compare:                           # compare result vs reference
la          t0, ref_result
add         t0, t0, s0
lwu         t1, 0(t0)
xor         gp, t1, a0              # compare
bnez        gp, _exit               # go to exit if not equal
addi        s0, s0, 4               # step result index for 4-byte

addi        s2, s2, 1               # step column index
blt         s2, s4, __mmul_col      # column index < 4 ?

addi        s1, s1, 1               # step row index
li          s2, 0                   # reset column index
blt         s1, s3, __mmul_row      # row index < 4 ?


#===========================================================
.global _exit
_exit:                          # exit: infinity loop
j           _exit


#===========================================================
.data
.align 2
byte_matrix_row:
.dword  0x0000000000000004
byte_matrix_col:
.dword  0x0000000000000004
byte_matrix_a:
.word   0x9157D42A
.word   0x8739AC14
.word   0xCE87D325
.word   0x2EBBB46C
byte_matrix_b:
.word   0x7FA511C8
.word   0xBD8780FF
.word   0x35B188B2
.word   0xAF15A3D1
ref_result:
.word   0x0001A6DB
.word   0x0000F755
.word   0x0000D2EA
.word   0x0001267C
.word   0x000150CD
.word   0x0000CB91
.word   0x00009A14
.word   0x0000F0FE
.word   0x0001F521
.word   0x000136D7
.word   0x0000F55B
.word   0x000156E7
.word   0x0001AF40
.word   0x0000E1CE
.word   0x00012999
.word   0x000100A1

.align 5
.dword  0x0000000000000000
.dword  0x0000000000000000
.dword  0x0000000000000000
.dword  0x0000000000000000
.dword  0x0000000000000000
.dword  0x0000000000000000
.dword  0x0000000000000000
.dword  0x0000000000000000
.dword  0x0000000000000000
.dword  0x0000000000000000
.dword  0x0000000000000000
.dword  0x0000000000000000
.dword  0x0000000000000000
.dword  0x0000000000000000
.dword  0x0000000000000000
.dword  0x0000000000000000
.dword  0x0000000000000000
.dword  0x0000000000000000
.dword  0x0000000000000000
.dword  0x0000000000000000
.dword  0x0000000000000000
.dword  0x0000000000000000
.dword  0x0000000000000000
.dword  0x0000000000000000
.dword  0x0000000000000000
.dword  0x0000000000000000
.dword  0x0000000000000000
.dword  0x0000000000000000
.dword  0x0000000000000000
.dword  0x0000000000000000
.dword  0x0000000000000000
.dword  0x0000000000000000
stack:
.dword  0x0000000000000000
