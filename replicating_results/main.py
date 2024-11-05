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
   
   #Making quiver plots for at 50
   fig, ax= plt.subplots(figsize=(6,6))
   qv = ax.quiver(pos[50][:,0], pos[50][:,1], np.cos(theta[50]), np.sin(theta[50]), s[50], clim=[0, 1])
   ax.set_xlabel('x')
   ax.set_ylabel('y')
   plt.show()
   plt.savefig(name+"_quiver_step_50.png")
   plt.close()
    
   #Making quiver plots for at last step
   fig, ax= plt.subplots(figsize=(6,6))
   qv = ax.quiver(pos[-1][:,0], pos[-1][:,1], np.cos(theta[-1]), np.sin(theta[-1]), s[-1], clim=[0, 1])
   ax.set_xlabel('x')
   ax.set_ylabel('y')
   plt.show()
   plt.savefig(name+"_quiver_last_step.png")
   plt.close()
   
   #Making the animation
   anim=animate(pos,theta,s,1000)
   anim.save(name+"_animate.gif")
   plt.close()

print("a Has started")
Run(0.2,"a")
print("b Has started")
Run(2,"b")
print("c Has started")
Run(8,"c")
