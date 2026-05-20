# Liam Archer 01/15/2026

#Imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create Angstrom symbol
Angstrom = '\u00C5'

# Read data into pandas
#df_3 = "powerlaw_only.dat"
#df_po = pd.read_csv(df_3, skiprows=3, delim_whitespace=True, names=["Angstrom", "Angstrom_err", "Counts/s/Angstrom", "Counts/s/Angstrom_err", 'Model_fit'])
#print(df_po.head())

df_1 = "OVIII_no_gauss_norm.dat"
df = pd.read_csv(df_1, skiprows=3, delim_whitespace=True, names=["Angstrom", "Angstrom_err", "Counts/s/Angstrom", "Counts/s/Angstrom_err", 'Model_fit'])
#print(df.head())

df_2 = "OVIII_gauss_norm.dat"
df_new = pd.read_csv(df_2, skiprows=3, delim_whitespace=True, names=["Angstrom", "Angstrom_err", "Counts/s/Angstrom", "Counts/s/Angstrom_err", 'Model_fit'])
#print(df_new.head())

#xMin = min(df['Angstrom'])
#xMax = max(df['Angstrom'])

fig, ax = plt.subplots(figsize=(10,6))
plt.errorbar(df['Angstrom'], df['Counts/s/Angstrom'], df['Counts/s/Angstrom_err'], fmt = '.', color = 'black', label='XSPEC Data')
df.plot(x = 'Angstrom', y = 'Model_fit', ax = ax, kind = 'line', color = 'blue', label = 'No Gaussian normalization')
df_new.plot(x = 'Angstrom', y = 'Model_fit', ax = ax, kind = 'line', color = 'red', label = 'With Gaussian normalization')
#df_po.plot(x = 'Angstrom', y = 'Model_fit', ax = ax, kind = 'line', color = 'green', label = 'PowerLaw only')
ax.set_title('Gaussian Model Comparison with Xspec Data for OVIII Absorption Lines')
ax.set_xlabel(f'Wavelength({Angstrom})')
ax.set_ylabel(f'Counts/s/{Angstrom}')
ax.set_xlim(16.99,23)
ax.legend(loc='best') # Add a legend to differentiate the lines
ax.grid(True) # Add a grid for better readability
plt.tight_layout() # Adjust layout to prevent overlapping elements
plt.savefig('Gauss_model_comparison_OVIII_clean.png')
plt.show()
quit()