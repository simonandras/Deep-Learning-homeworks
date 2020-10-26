
import numpy as np


data = np.genfromtxt('budapest_wheather_data.csv', delimiter='\t')
np.save('data.npy', data)

