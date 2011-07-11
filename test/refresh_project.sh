#!/bin/bash
echo jumping to upper dir \(where can find pigs\/ \) ..
cd ../
MYLS=$(pwd)
echo now at: $MYLS
echo refreshing..
find pigs/ -name '*.pyc' -exec rm {} \;
echo finish refreshing
MYFIND=$(find pigs/ -name '*.pyc')
echo check if any .pyc left: $MYFIND
