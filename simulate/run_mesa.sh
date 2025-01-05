#!/bin/bash
echo Begining simulation job $2
python3 ./run_iter.py $1 $2 # Argument 1 is the thread number, argument 2 is the index in the data file
cd ./run/$1 && ./rn
cd ../..
# Save the history file
mkdir -p ./LOGS/$1/$2
cp ./run/$1/LOGS/* ./LOGS/$1/$2/
echo Simulation job $1.$2 finished
