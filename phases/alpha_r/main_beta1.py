from  Vicsek_modified_conditional  import *
import numpy as np


#Function that stores what the final average s for the particles for different r and alpha
def generate_phase(eta,file_name):
    L=31.6
    rho=0.5
    N=int(rho*L**2)

    v_0=0.1
    iterations=2000
    beta=1

   
    r_list=np.linspace(2,5,20)
    alpha_list=np.linspace(0,4,20)

    final_s=np.zeros([len(alpha_list),len(r_list)])

    for a,alpha in enumerate(alpha_list):
       for e,r in enumerate(r_list):
            pos,theta,s=Vicsek_modified_conditional(v_0,eta,r, N,L,iterations,alpha,beta)
            #If this is one everyone cooperates if 0 no cooperates. If neither not enough iterations were given
            final_s[a][e]=sum(s[-1])/len(s[-1])

    np.save(file_name,final_s)

print("0 started")
generate_phase(0,"phase_beta1_eta0")
print("pi/8 started")
generate_phase(np.pi/8,"phase_beta1_eta_pi_over8")
print("pi/4 started")
generate_phase(np.pi/4,"phase_beta1_eta_pi_over4")
print("pi/2 started")
generate_phase(np.pi/2,"phase_beta1_eta_eta_pi_over2")
