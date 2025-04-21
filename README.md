# Effect of fuel density and temperature on helium-3 fusion reaction rates in stellar cores

This repository contains the full code used to conduct this research including files before major method changes (which
makes them obsolete).

For purposes of reproducing the results, please see the `mesa_data_prep.ipynb` and `simulation_collation.ipynb` files
which
are the final codes used to prepared, conduct, and analyze the data.

## Data

The final stellar data after simulations can be found in `stellar_profiles.json`.

All pre-processed simulation inputs can be found in `simulate/data.csv`.

## Running the simulations

After installing MESA, you will need to build the template simulation using the `mk` script in the `simulate/template`
directory.

Then, simply run the `./rn` file in the `simulate` directory to run the simulations. The system I used had 8 cores and
16 threads so the `rn` script executes GNU parallel in 4 jobs with 4 threads each.

Ensure to set the `OMP_NUM_THREADS` (dictates the number of threads each MESA instnace uses.) environment variable to
the appropriate number of threads for your system.

So, `OMP_NUM_THREADS=(number of threads / number of jobs)`.