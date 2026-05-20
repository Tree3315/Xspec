# Liam Archer 01/09/2026
# Determine what Chi-Squared Distribution is statistically significant

# Imports
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import chi2

# Import capital delta symbol
Delta = '\u0394'

# Important constants
eps = 0.001
dof = 1 # Number of degrees of freedom

# Determine singular value of Chi-squared distribution
value = 3.47
value_check = chi2.cdf(value,dof)*100
print(value, value_check)

# Calculate p-value
p = 1-(value_check/100)
print('p-value =',round(p,4))

# Plot cumulative Chi-squared distribution
xaxis = np.linspace(eps, 10)
yaxis = chi2.cdf(xaxis,dof)
plt.subplots(figsize = (10,6))
plt.plot(xaxis, yaxis, color = 'blue', label = 'Chi-squared cdf')
plt.vlines(value,eps,1, linestyles = 'dotted', color = 'red', label = (f'{Delta}C value')) # Straight line where intersection occurs
plt.ylim(0,1)
plt.yticks(np.arange(0,1,0.1))
plt.xlabel(f'{Delta}C Value')
plt.ylabel('Probability')
plt.title(f'{Delta}C vs Chi-Squared CDF of One Degree of Freedom')
plt.legend(loc='upper right')
plt.tight_layout()
plt.savefig('Chi-Squared_with_Delta_C_OVII.png')
plt.show()
quit()
