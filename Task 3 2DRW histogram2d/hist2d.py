    #3D plotting section
    fig, ax = plt.subplots(1, subplot_kw=dict(projection="3d"))
    h, xbins, ybins = np.histogram2d(x_final,y_final, bins=10)
    
    # creating a mesh grid 
    xgrid, ygrid = np.meshgrid(xbins[:-1], ybins[:-1])
    bottom = 0*xgrid
    
    # width and depth of bar graph will be the bin size
    width = xbins[1]-xbins[0]
    depth = ybins[1]-ybins[0]
    
    # feed everything into bar3d!
    ax.bar3d(xgrid.flatten(), ygrid.flatten(), bottom.flatten(), width, depth, h.flatten(), shade=True)
    ax.set_title('2D Histogram for 2D Random Walk')