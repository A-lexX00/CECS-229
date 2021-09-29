.data
A: .byte 2,0,3,1
.text
li x5, 4 
li x6, 2
la x10, A
addi x7, x0, 0
Loop1:
bge x7, x5, exit1
addi x29, x0, 0
Loop2:
bge x29, x6, exit2
add x3, x10, x7
lb x1, 0(x3) 
add x1, x1, x7
slli x2, x29, 2
add x2, x2, x29
add x1, x1, x2
sb x1, 0(x3)
addi x29, x29, 1
Exit2:
addi x7, x7, 1
j Loop1
Exit1: