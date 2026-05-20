# Liam Archer 01/31/2026

#Imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from astropy.cosmology import FlatLambdaCDM
from astropy import constants as const
from astropy import units as u

# Create Angstrom symbol
Angstrom = '\u00C5'

# Calculate equivalent width from OVII data
df_1 = "OVII_flux_correct.dat"
df = pd.read_csv(df_1, skiprows=3, delim_whitespace=True, names=["Angstrom", "Angstrom_err", "Flux", "Flux_err", 'Model_fit'])
print(df.head())

flux_avg_OVII = np.average(df['Flux'])
print("Flux Average:", f'{flux_avg_OVII:.4E}')

#gaussian_norm = -3.5755E-5
gaussian_norm_OVII = -4.4564E-5
print("K:",gaussian_norm_OVII)

equivalent_width_OVII = (gaussian_norm_OVII/flux_avg_OVII)
print('Equivalent width:', f'{np.abs(equivalent_width_OVII):.4E}')

# Calcualte the column denisty of WHIM using equivalent width
wavelength_OVII = 21.602 # Angstroms
wavelength_OVIII = 18.97

f = 0.696 # Oscillatory Strength of OVII
f_OVII = 0.426

N_OVII = 1.13E20*(equivalent_width_OVII/((wavelength_OVII**2)*(f))) # cm**-2
print('Column Density of OVII:',f'{np.abs(N_OVII):.4E}')

#N_OVIII = 1.13E20*(equivalent_width_OVII/((wavelength_OVIII**2)*(f_OVII))) # cm**-2
#print('Column Density of OVIII:',f'{np.abs(N):.4E}')

# Manual Redshift Calculation

# The redshifts in question
redshift = .0902
#redshift_new = .0891
redshift_new = 0.0888

c = 3E5 # km/s

Hubble_constant = 70 #km/s/Mpc

distance_Mpc = redshift*c/Hubble_constant
print('Redshift distance in Mpc',round(distance_Mpc,3))
distance_Mpc_new = redshift_new*c/Hubble_constant
print('Redshift distance in Mpc',round(distance_Mpc_new,3))
diff_dist_man = distance_Mpc-distance_Mpc_new
print('Difference in redshifted distance is',round(diff_dist_man,3))


# Initialize Cosmological Model
cosmo = FlatLambdaCDM(H0=70, Om0=0.3)
#print(cosmo)

# The astropy official method

# Define Hubble Constant
H0= Hubble_constant*u.km/u.s/u.Mpc
print(H0)

# Convert speed of light to km/s
c = const.c.to('km/s')
print(c)

# Calculate redshift differential when z<<1
d = (redshift*c/H0)
print('Accurate distance for redshift of',redshift,'is',round(d,3))
d_other = (redshift_new*c/H0)
print('Accurate distance for redshift of',redshift_new,'is',round(d_other,3))

dist_diff = d-d_other
print('Difference in redshifted distance is',round(dist_diff,3))