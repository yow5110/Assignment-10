def rw2d_multi(Np, Nstep):
    """
    A simulation for 2D random walk.
    Np = the number of particles simulated
    Nstep = the number of steps each particle takes
    """

    Nstep=int(Nstep)
    Np = int(Np)
    
    rng = np.random.default_rng()

    # Individual steps in x and y
    angles = # a 2D array of dimensions Np x Nstep
    x_list = # a 2D array of dimensions Np x Nstep
    y_list = # a 2D array of dimensions Np x Nstep
    
    # Final x,y positions of all particles
    # No need to record their trajectories  
    x_final =  # a 1D array of size Np using np.sum
    y_final =  # a 1D array of size Np using np.sum
    
    fig, ax1 = plt.subplots(1)
    ax1.plot(x_final, y_final, 'ro')
    ax1.set_aspect('equal', 'box')
    plt.show()
        
rw2d_multi(Np=1e3, Nstep=1e4)