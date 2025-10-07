for i in $(seq 0 48)
    do
        echo "Running $i"
        time ./run_mesa.sh 0 $i # Argument 1 is the thread number, argument 2 is the index in the data file
        echo "Done"
    done
    