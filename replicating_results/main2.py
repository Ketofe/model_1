import sys
import os

#This code is to enable src accses 

# Get the absolute path to the 'src' directory
folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src_path = os.path.join(folder, 'src')

# Add the 'src' directory to sys.path
if src_path not in sys.path:
    sys.path.append(src_path)






from Vicsek_modified import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from order import *
from animate import *









#Function that runs the mofidided vicsek and creates plots and 
def Run(r,name):
   rho =1
   L=31.6
   N = int(rho*L**2 )
   v_0=0.1
   iterations = 10000
   eta=0.5
   alpha=1
   beta=1
   
   pos,theta,s=Vicsek_modified(v_0,eta,r, N,L,iterations,alpha,beta)

   np.save("pos_"+name,pos)
   np.save("theta_"+name,theta)
   np.save("s_"+name,s)


print("a Has started")
Run(0.2,"a")
print("b Has started")
Run(2,"b")
print("c Has started")
Run(8,"c")
