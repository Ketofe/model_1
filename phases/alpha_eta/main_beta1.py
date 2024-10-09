from  Vicsek_modified_conditional import *
import numpy as np


#Function that generates the data for different eta and alpha
def generate_phase(r):
    L=31.6
    rho=0.5
    N=int(rho*L**2)

    v_0=0.1
    iterations=2000
    beta=1

    eta_list=np.linspace(0,np.pi,20)
    alpha_list=np.linspace(0,4,20)

    final_s=np.zeros([len(alpha_list),len(eta_list)])

    for a,alpha in enumerate(alpha_list):
       for e,eta in enumerate(eta_list):
            pos,theta,s=Vicsek_modified_conditional(v_0,eta,r, N,L,iterations,alpha,beta)
            #If this is one everyone cooperates if 0 no cooperates. If neither not enough iterations were given
            final_s[a][e]=sum(s[-1])/len(s[-1])
    np.save("beta1_pahse_plot_r"+str(r),final_s)



rs=[5,4,3,2,1]

for r in rs:
     print(r)
     generate_phase(r)

