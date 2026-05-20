# Liam Archer 02/06/2026
# Create graphical models of the OVII and OVIII Flux Density

#Imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create Angstrom symbol
Angstrom = '\u00C5'

df_1 = "OVII_flux_correct.dat"
df = pd.read_csv(df_1, skiprows=3, delim_whitespace=True, names=["Angstrom", "Angstrom_err", "Counts/cm**-2/s/Angstrom", "Counts/cm**-2/s/Angstrom_err","Pow+Zagauss","Powerlaw", 'Zagauss'])
print(df.head())

df_2 = "OVII_flux_correct_no_gauss_norm.dat"
df1 = pd.read_csv(df_2, skiprows=3, delim_whitespace=True, names=["Angstrom", "Angstrom_err", "Counts/cm**-2/s/Angstrom", "Counts/cm**-2/s/Angstrom_err","Pow+Zagauss","Powerlaw", 'Zagauss'])
print(df1.head())

fig, ax = plt.subplots(figsize=(10,6))
plt.errorbar(df['Angstrom'], df['Counts/cm**-2/s/Angstrom'], df['Counts/cm**-2/s/Angstrom_err'], fmt = '.', color = 'black', label='XSPEC Flux Data')
df1.plot(x = 'Angstrom', y = 'Pow+Zagauss', ax = ax, kind = 'line', color = 'blue', label = 'No Gauss Norm')
df.plot(x = 'Angstrom', y = 'Pow+Zagauss', ax = ax, kind = 'line', color = 'red', label = 'Gauss Norm')
ax.set_title('Wavelength vs Photon Flux Density for OVII')
ax.set_xlabel(f'Wavelength({Angstrom})')
#ax.set_ylabel(rf'Counts/$\mathregular{{cm^-2}/{s^-1}/{Angstrom}^-1}$')
ax.set_ylabel(r'Counts $\mathregular{cm^{-2}}$ $\mathregular{s^{-1}}$ $\mathregular{\AA^{-1}}$')
ax.set_xlim(20,26)
ax.legend(loc='best') # Add a legend to differentiate the lines
ax.grid(True) # Add a grid for better readability
plt.tight_layout() # Adjust layout to prevent overlapping elements
plt.savefig('Gauss_model_comparison_OVII_flux_density_correct.png')
plt.show()
quit()