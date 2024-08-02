python ./setup.py

for i in $(seq 920 2000)
do
    echo "Running $i"
    time ./run_mesa.sh $i
    echo "Done"
done
