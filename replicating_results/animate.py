import numpy as np
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt 
#https://francescoturci.net/2020/06/19/minimal-vicsek-model-in-python/ was used to make this


def animate(pos,theta,s,number_of_frames):

        fig, ax= plt.subplots(figsize=(6,6))
            

        qv=ax.quiver(pos[0][:,0], pos[0][:,1], np.cos(theta[0]), np.sin(theta[0]), s[0], clim=[0, 1])

        # Animation function
        def animate(i):
            

            qv.set_offsets(pos[i])
            qv.set_UVC(np.cos(theta[i]), np.sin(theta[i]),s[i])
           
            
            
            return qv,

        anim = FuncAnimation(fig,animate,np.arange(1, number_of_frames),interval=1, blit=True)
        plt.show()
        return anim

