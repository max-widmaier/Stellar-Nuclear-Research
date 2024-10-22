#!/bin/bash
echo Begining simulation job $2
python3 ./run_iter.py $1 $2 # Argument 1 is the thread number, argument 2 is the index in the data file
cd ./run/$1 && ./rn
cd ../..
# Save the history file
cp ./run/$1/LOGS/history.data ./LOGS/$1/history_$2.data
echo Simulation job $2 finished