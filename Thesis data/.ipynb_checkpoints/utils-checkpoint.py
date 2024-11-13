import numpy as np

def radial_average(input_array, box_dims, kbins=10, binning='log', breakpoint=0.1):
    k_comp, k = _get_k(input_array, box_dims)

    kbins = _get_kbins(kbins, box_dims, k, binning=binning, breakpoint=breakpoint)

    dk = (kbins[1:]-kbins[:-1])/2.

    outdata = np.histogram(k.flatten(), bins=kbins, weights = input_array.flatten())[0]

    n_modes = np.histogram(k.flatten(), bins=kbins)[0].astype('float')
    outdata /= n_modes

    return outdata, kbins[:-1]+dk, n_modes

def _get_k(input_array, box_dims):
    '''
    Get the k values for input array with given dimensions.
    Return k components and magnitudes.
    For internal use.
    '''
    dim = len(input_array.shape)
    if dim == 1:
        x = np.arange(len(input_array))
        center = x.max()/2.
        kx = 2.*np.pi*(x-center)/box_dims[0]
        return [kx], kx
    elif dim == 2:
        x,y = np.indices(input_array.shape, dtype='int32')
        center = np.array([(x.max()-x.min())/2, (y.max()-y.min())/2])
        kx = 2.*np.pi * (x-center[0])/box_dims[0]
        ky = 2.*np.pi * (y-center[1])/box_dims[1]
        k = np.sqrt(kx**2 + ky**2)
        return [kx, ky], k
    elif dim == 3:
        nx,ny,nz = input_array.shape
        x,y,z  = np.indices(input_array.shape, dtype='int32')
        center = np.array([nx/2 if nx%2==0 else (nx-1)/2, ny/2 if ny%2==0 else (ny-1)/2, \
                            nz/2 if nz%2==0 else (nz-1)/2])
        kx = 2.*np.pi * (x-center[0])/box_dims[0]
        ky = 2.*np.pi * (y-center[1])/box_dims[1]
        kz = 2.*np.pi * (z-center[2])/box_dims[2]

        k = np.sqrt(kx**2 + ky**2 + kz**2 )
        return [kx,ky,kz], k

def _get_kbins(kbins, box_dims, k, binning='log', breakpoint=0.1):
    '''
    Make a list of bin edges if kbins is an integer,
    otherwise return it as it is.
    '''
    if isinstance(kbins,int):
            kmin = 2.*np.pi/min(box_dims)
            if binning=='linear': kbins = np.linspace(kmin, k.max(), kbins+1)
            elif binning=='log': kbins = 10**np.linspace(np.log10(kmin), np.log10(k.max()), kbins+1)
            else:
                    kbins_low  = np.linspace(kmin, k.max(), kbins+1)
                    kbins_high = 10**np.linspace(np.log10(kmin), np.log10(k.max()), kbins+1)
                    kbins = np.hstack((kbins_low[kbins_low<breakpoint],kbins_high[kbins_high>breakpoint]))
    return kbins