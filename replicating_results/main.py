from Vicsek_modified import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from order import *

#Function that runs the mofidided vicsek and creates plots and 
def Run(r,name):
   rho =1
   L=31.6
   N = int(rho*L**2 )
   v_0=0.1
   iterations = 10000
   eta = 11
   alpha=1
   beta=1
   
   pos,theta,s=Vicsek_modified(v_0,eta,r, N,L,iterations,alpha,beta)

   o=[order(t) for t in theta]
   C=[sum(t)/len(t) for t in s]
   plt.plot(C,label='fraction of cooroperators')
   plt.plot(o,label='order')
   plt.xscale('log')
   plt.xlabel('iterations')
   plt.legend()
   plt.show()
   plt.savefig(name+"_plot.png")
   plt.close()
   
   #Making quiver plots for at 100
   fig, ax= plt.subplots(figsize=(6,6))
   qv = ax.quiver(pos[100][:,0], pos[100][:,1], np.cos(theta[100]), np.sin(theta[100]), s[100], clim=[0, 1])
   plt.show()
   plt.savefig(name+"_quiver_step_100.png")
   plt.close()
    
   #Making quiver plots for at last step
   fig, ax= plt.subplots(figsize=(6,6))
   qv = ax.quiver(pos[-1][:,0], pos[-1][:,1], np.cos(theta[-1]), np.sin(theta[-1]), s[-1], clim=[0, 1])
   plt.show()
   plt.savefig(name+"_quiver_last_step.png")
   plt.close()
   
   

print("a Has started")
Run(0.2,"a")
print("b Has started")
Run(2,"b")
print("c Has started")
Run(8,"c")
