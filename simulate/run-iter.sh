python ./setup.py

for i in $(seq 0 1999)
do
    echo "Running $i"
    time ./run_mesa.sh $1 $i # $1 is the thread number, $i is the index
    echo "Done"
done
