#!/bin/bash

SIZE=256
GAP=15

ROWSTOT=$SIZE
COLSTOT=$SIZE

ROWS=$(($ROWSTOT-2*$GAP))
COLS=$(($COLSTOT-(2*$GAP)))
ROWSH=$(($ROWS/2))
COLSH=$(($COLS/2))

A="."
B="W"


printline()
{
for ((i=1;i<=$1;i++))
   do
       echo -n "$2"
   done
}   





for ((j=1;j<=$GAP;j++))
do
   printline $COLSTOT $A
   echo
done

for ((j=1;j<=$ROWSH;j++))
do
   printline $GAP $A 
   printline $((($COLSH-$j))) $A
   printline $((j*2)) $B
   printline $(($COLSH-$j)) $A
   printline $GAP $A 
   echo
done

for ((j=1;j<=$ROWSH;j++))
do
   printline $GAP $A 
   printline $j $A
   printline $((($COLSH-$j)*2)) $B
   printline $j $A
   printline $GAP $A 
   echo
done

for ((j=1;j<=$GAP;j++))
do
   printline $COLSTOT $A
   echo
done

