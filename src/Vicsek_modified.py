import numpy as np
from scipy.spatial import cKDTree
#from snnpy import build_snn_model





                                                         #Here one can set initial conditions if not they wil be set to default values further down
def Vicsek_modified(v_0,eta,r, N,L,iterations,alpha,beta,initial_pos=None,initial_theta=None,initial_s=None):
        theta=np.zeros([iterations,N])
        pos=np.zeros([iterations,N,2])
       
        if initial_pos is None:
               initial_pos= [ [np.random.uniform(0,L),np.random.uniform(0,L) ] for k in range(N) ]
        pos[0]=initial_pos
       
        if initial_theta is None:
               initial_theta=np.random.uniform(-np.pi,np.pi,N)
        theta[0]=initial_theta
        
        #Creating the s
        if initial_s is None:
           initial_s=[ 1 if k%2==0 else 0 for k in range(N) ]
        s=np.zeros([iterations,N])
        s[0]=initial_s

        

        for iteration in range(iterations-1):
                #Updating the postions 
                pos[iteration + 1] = (pos[iteration] + v_0 * np.stack([np.cos(theta[iteration]), np.sin(theta[iteration])], axis=-1)) % L
               
                


                #Here the neighbotrs are found
 
                tree = cKDTree(pos[iteration],boxsize=[L,L])     #Added workers beneath for parallel processing
                negibors=tree.query_ball_point(pos[iteration],r,workers=-1 ) 
                
               # snn_model = build_snn_model(pos[iteration])
               # negibors=[snn_model.query_radius(k, r) for k in pos[iteration]]


               #This is made using chat gpt
                # Filter out the particle's own index from its neighbors list 
                for particle_index in range(N):
                          negibors[particle_index] = [i for i in negibors[particle_index] if i != particle_index]
                
                #Now looping over all the particles and doing the angle and s updates
                for particle_index in range(N):
                      negibor_indexes=negibors[particle_index]
                      #The angles of the neigbors
                      angles=theta[iteration][negibor_indexes]
                                                              
                      if s[iteration][particle_index]==1:    
                             angle_average=np.angle( np.exp( theta[iteration][particle_index]*1j )+sum(np.exp(angles*1j) )    )
                             theta[iteration+1][particle_index]=angle_average+np.random.uniform(-eta,eta)
                             
                      else:
                              #Choosing random angle
                             theta[iteration+1][particle_index]=np.random.uniform(-np.pi,np.pi)
                           

                      #Making sure there neibors                        
                      if len( negibor_indexes)!=0:
                               #Picking a random neigbor
                               random_neigbor=np.random.choice( negibor_indexes)
                      
                               #No need to update s if they are already the same. 
                               if s[iteration][particle_index]!=s[iteration][random_neigbor]:
                        



                               

                                                                                           #Divinding by the amount of neighbors                       
                                       r1=sum(np.cos( 0.5*(theta[iteration][particle_index]-angles ))  )/len(negibor_indexes)

                                       #The cost
                                       P1=r1-alpha*s[iteration][particle_index]*r/L

                                       #Doing the same with its neigbor
                      
                                        #Neigbor's neigbors
                                       negibor_indexes2=negibors[random_neigbor]
                                       angles2=theta[iteration][negibor_indexes2]                         #Dividing by the amount of neigbors
                                       r2=sum(np.cos( 0.5*(theta[iteration][random_neigbor]-angles2 ))  )/len(negibor_indexes2)
                                       P2=r2-alpha*s[iteration][ random_neigbor]*r/L


                        
                                        #Making the probabilitstic choice
                                       if np.random.uniform(0,1)<1/(1+np.exp((P1-P2)/beta)):
                                           s[iteration+1][particle_index]=s[iteration][ random_neigbor]
                                       else:  
                                           s[iteration+1][particle_index]=s[iteration][particle_index]

                               else:  
                                      s[iteration+1][particle_index]=s[iteration][particle_index]
                        
                        
                      else:
                           s[iteration+1][particle_index]=s[iteration][particle_index]

                     
        return pos,theta,s   







