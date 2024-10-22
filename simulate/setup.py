import os
import shutil

import numpy as np
import pandas as pd

data = pd.read_csv('data.csv')
SPECTROSCOPY_ATOMS = ['C', 'O', 'N', 'Ne', 'Mg', 'Al', 'Si', 'S', 'K', 'Ca', 'Ti', 'Cr', 'Mn', 'Fe', 'Ni']

N_THREADS = 4

for i in range(N_THREADS):
    if not os.path.exists(f'./run/{i}'):
        # Copy full template
        os.system(f'cp -r ./template ./run/{i}')
    else:
        # Otherwise just copy inlist_project
        shutil.copy('template/inlist_project', f'./run/{i}/inlist_project')

    if not os.path.exists(f'./LOGS/{i}'):
        os.system(f'mkdir -p ./LOGS/{i}')

data_len = len(data)
size = data_len // N_THREADS
for i in range(N_THREADS):
    dir_name = f'./run/{i}'
    if i < N_THREADS:
        data_split = data.iloc[i * size:(i + 1) * size, :]
    else:
        data_split = data.iloc[i * size:, :]

    data_split.to_csv(f'{dir_name}/data.csv', index=False)
    row = data_split.iloc[0]

    with open(dir_name + '/inlist_project', 'r') as f_read:
        content = f_read.read()
        with open(dir_name + '/inlist_project', 'w') as f:
            content = content.replace('{star_mass}', str(row['mass']))
            content = content.replace('{star_helium}', str(row['y']))
            content = content.replace('{star_metallicity}', str(row['z']))
            content = content.replace('{star_age}', str(row['age']))

            for atom in SPECTROSCOPY_ATOMS:
                atom_replace = atom.lower()
                param_name = f'${atom_replace}_mass_frac$'
                if not np.isnan(row[f'{atom}_mass_frac']) and row[f'{atom}_mass_frac'] > 0:
                    content = content.replace(param_name, f'z_fraction_{atom_replace} = {row[f"{atom}_mass_frac"]}')
                else:
                    content = content.replace(param_name, f'! {atom}_mass_frac is nan and has been ignored')

            f.write(content)

    with open(f'./run-iter_{i}.sh', 'w') as f:
        f.write(f"""for i in $(seq 0 {len(data_split) - 1})
    do
        echo "Running $i"
        time ./run_mesa.sh {i} $i # Argument 1 is the thread number, argument 2 is the index in the data file
        echo "Done"
    done
    """)


