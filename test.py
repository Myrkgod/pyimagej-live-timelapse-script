from glob import glob
import imagej, time, argparse
import numpy as np
import imagej.dims as dims
import xarray as xr

ij = imagej.init(mode='gui')
print(f"ImageJ version: {ij.getVersion()}")


xarray = xr.DataArray(data=None)
print(xarray)

dataset = ij.io().open('MIPs/Scan_Iter_0000_0000_CamA_ch0_CAM1_stack0000_488nm_0000000msec_0106060251msecAbs_MIP_z.tif')
data_xarray = xarr = ij.py.from_java(dataset)

new_stack = xr.concat((data_xarray, data_xarray), dim='ch')
print(f"Number of dims: {len(new_stack.dims)}\ndims: {new_stack.dims}")
print(new_stack[0])

new_dataset_4d = ij.py.to_java(new_stack)
ij.ui().show(new_dataset_4d)