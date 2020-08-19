# Name: Breanna Shinn
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.

from importlib import reload as Rfrsh
import hmmm

RecFibSeq = """ 
00 read r1
01 setn r15 42
02 setn r2 1
03 copy r3 r1
04 setn r4 2
05 nop 
06 calln r14 13

07 mod r3 r3 r4
08 jeqzn r3 11

09 write r2
10 halt

11 write r13
12 halt

13 jnezn r1 21
14 setn r13 0
15 nop
16 jumpr r14

17 jnezn r1 29
18 setn r13 0
19 nop
20 jumpr r14

21 pushr r14 r15
22 addn r1 -1
23 nop
24 calln r14 17
25 nop

26 popr r14 r15
27 add r13 r2 r13
28 jumpr r14

29 pushr r14 r15
30 addn r1 -1
31 nop
32 calln r14 13
33 nop

34 popr r14 r15
35 add r2 r2 r13
36 jumpr r14
 
"""

# Change doDebug to false to turn off debugs
runThis = RecFibSeq
doDebug = False

# Note: main() in the shell to easily reload
def main(runArg=runThis,  debugArg=doDebug):
    Rfrsh(hmmm); hmmm.main(runArg, debugArg)

if __name__ == "__main__" :
    main()
