from glob import glob
import imagej, time, argparse
import numpy as np
import imagej.dims as dims
import xarray as xr


fetch_interval = 10
directory = 'MIPs'
channel_list = ['CamA_ch0']

def add_image(file_list):
    print(file_list)
    tif_list = []
    for image in file_list:
        tif_list.append(tifffile.imread(str(image), name='CamA'))
    timelapse = np.asarray(tif_list)
    new_dataset_4d = ij.py.to_java(timelapse)
    ij.ui().show(new_dataset_4d)
    time.sleep(10)

def fetch_files():
    while True:
	    old_files = set()
	    new_files = set()

	    for file in sorted(directory.glob(zip('CamA', 'CamB')+'.tif')):
	        print(file)
	        if file not in old_files:
	            new_files.add(file).difference_update(old_files)
	            old_files.add(file)

	    for channel in channel_list:
	        file_list = []
	        for file in new_files:
	            if channel in file:
	                file_list.append(file)
	        add_image(file_list)

# initialize ImageJ
ij = imagej.init('net.imagej:imageJ:2.1.0')	
fetch_files()
