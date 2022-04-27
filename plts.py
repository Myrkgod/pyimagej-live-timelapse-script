from glob import glob
import imagej, time, argparse
import numpy as np
import imagej.dims as dims
import xarray as xr


fetch_interval = 10
directory = 'MIPs'
channel_list = ['CamA_ch0']

def fetch_files():
    old_files = []
    new_files = []
        
    for file in sorted(glob(directory+'/*tif')):
        if file not in old_files:
            new_files.append(file)
            old_files.append(file)

    for channel in channel_list:
        file_list = []
        for file in new_files:
            if channel in file:
                file_list.append(file)
        add_image(file_list)

def add_image(file_list):
	print(file_list)
	dataset_4d = ij.io().open(file_list[0])
	xarr_4d = ij.py.from_java(dataset_4d)
	print(f"xarr/numpy shape: {xarr_4d.shape}")
	for file in file_list[1:]:
		print(file)
		dataset_2d = ij.io().open(file)
		xarr_2d = ij.py.from_java(dataset_2d)
		xarr_4d = xr.concat((xarr_2d, xarr_4d), dim='time')
		print(f"xarr/numpy shape: {xarr_4d.shape}")


# initialize ImageJ
ij = imagej.init('net.imagej:imageJ:2.1.0')	
fetch_files()
