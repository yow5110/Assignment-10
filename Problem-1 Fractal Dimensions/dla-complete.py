import numpy as np
import matplotlib.pyplot as plt

def rw2d(x0,y0,N):
    N=int(N)
    
    rng = np.random.default_rng()
    angles = np.array(np.arange(0,360,90))
    stepx = np.cos(angles/180*np.pi)
    stepy = np.sin(angles/180*np.pi)
    step = np.transpose([stepx, stepy])
    
    hop_list =    rng.choice( step , N)
    
    x = np.cumsum(hop_list[:,0])
    y = np.cumsum(hop_list[:,1])
    return np.array([x0+x, y0+y]).T    

def check_intersec(traj, cluster):
    """
    traj: a 2D array with dimensions Nsteps x 2. Needs to be all integers.
    cluster: a 2D array with dimensions Cluster Size x 2. Needs to be all integers.
    
    Description: This function searches for the first time traj intersects with cluster.
    
    Returns: the index of traj immediately before the intersection,
    i.e. the element in traj to be appended to the growing cluster.
    If there is no intersection, it returns -1.
    """
    traj    = np.around(traj).astype(int)
    cluster = np.around(cluster).astype(int)
    traj = traj[:,0]+traj[:,1]*1j
    cluster= cluster[:,0] + cluster[:,1]*1j
    
    intersec = np.where(np.isin(traj,  cluster ))[0]
    idx = -1 #default return value
    if len(intersec) > 0:
        idx = intersec[0] - 1
        #to prevent accidentally returning negative values
        if idx < 0 : 
            idx = -1
    return idx
            
def dla():
    rng = np.random.default_rng()
    cluster = np.array([[0,0],[0,1]])

    Ns = 10000
    for i in range(Ns):
        cluster_max_radius = np.sqrt(cluster[:,0]**2+cluster[:,1]**2).max()
        
        
        spawn_radius = cluster_max_radius * 2
        if i%100==0: print(int(i/Ns*100),'%')
        angle = rng.uniform(0,2*np.pi)
        x0,y0 = int(spawn_radius * np.cos(angle)),  int(spawn_radius*np.sin(angle))
        traj = rw2d(x0,y0,1e4)
        
        idx = check_intersec(traj, cluster)
        if idx >0:
            cluster = np.append(cluster, [traj[idx]],axis=0)
            
    xplot = cluster[:,0]
    yplot = cluster[:,1]
    
    r=100
    intervals = 8
    color = plt.cm.rainbow(np.linspace(0, 1,intervals))
    plt.rcParams["axes.prop_cycle"] = plt.cycler("color", color )
    plt.figure()
    plt.xlim(-r,r)
    plt.ylim(-r,r)
    
    size = int(len(xplot)/intervals)
    for i in range(intervals):
        plt.plot(  xplot[i*size:(i+1)*size],   yplot[i*size:(i+1)*size] ,\
                 marker='.', linestyle='')
    print(len(xplot))

    plt.show()
    return cluster

dla()