#!/bin/bash
echo Begining simulation job $1
cp ./run/LOGS/history.data ./LOGS/history_$1.data
python3 ./run_iter.py $1
cd ./run && ./rn
echo Simulation job $1 finished
