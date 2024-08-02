## Copies the inlist_project file to the run directory ##
import pandas as pd
import numpy as np
import os
import shutil
import sys

index = int(sys.argv[1])
data = pd.read_csv('sim_batch_1500/data.csv')
SPECTROSCOPY_ATOMS = ['C', 'O', 'N', 'Ne', 'Mg', 'Al', 'Si', 'P', 'S', 'K', 'Ca', 'Ti', 'Cr', 'Mn', 'Fe', 'Ni']

if not os.path.exists('./run/'):
    # Copy full template
    os.system(f'cp -r ./template ./run/')
else:
    # Otherwise just copy inlist_project
    shutil.copy('template/inlist_project', './run/inlist_project')

dir_name = './run'
row = data.iloc[index]
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
