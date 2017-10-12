.data
var1: .asciiz"Enter the 1st numbers:"
var2: .asciiz"Enter the 2nd numbers:"
result: .asciiz"c="
.text
#a+3*(b+2)
main:
li $v0,4
la $a0,var1
syscall
li $v0,5
syscall
move $t0,$v0
li $v0,4
la $a0,var2
syscall
li $v0,5
syscall
move $t1,$v0
addi $t2,$t1,2
li $t3,3
mult $t3,$t2
mflo $t4
li $v0,4
la $a0 ,result
syscall
add $a0,$t0,$t4
li $v0,1
syscall
li $v0,10
syscall

