import numpy as np
#Function caculating the order in vicsek model

def order(angle_list):
    return np.sqrt(sum(np.sin(angle_list))**2+sum(np.cos(angle_list))**2 )/len(angle_list)
