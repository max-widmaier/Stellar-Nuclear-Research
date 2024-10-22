for i in $(seq 0 472)
    do
        echo "Running $i"
        time ./run_mesa.sh 1 $i # Argument 1 is the thread number, argument 2 is the index in the data file
        echo "Done"
    done
    