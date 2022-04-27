import h5py
filename = '/Users/saloniagrawal/Downloads/test.h5'
f=h5py.File(filename,'r')
list(f.keys())
#dset = f['dataset']


#dset.shape

#dset.dtype
