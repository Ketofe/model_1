from  Vicsek_modified_conditional  import *
import numpy as np


#Function that stores what the final average s for the particles for different r and eta
def generate_phase(alpha):
    L=31.6
    rho=0.5
    N=int(rho*L**2)

    v_0=0.1
    iterations=2000
    beta=1

   
    r_list=np.linspace(2,5,20)
    eta_list=np.linspace(0,np.pi,20)

    final_s=np.zeros([len(eta_list),len(r_list)])

    for a,eta in enumerate(eta_list):
       for e,r in enumerate(r_list):
            pos,theta,s=Vicsek_modified_conditional(v_0,eta,r, N,L,iterations,alpha,beta)
            #If this is one everyone cooperates if 0 no cooperates. If neither not enough iterations were given
            final_s[a][e]=sum(s[-1])/len(s[-1])

    np.save("phases_alpha"+str(alpha),final_s)

alphas=[0,0.5,1.5,2.5]

for alpha in alphas:
    print("alpha="+str(alpha)+"has started")
    generate_phase(alpha)
    
    
