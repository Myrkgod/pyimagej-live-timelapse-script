from pathlib import Path
import imagej
import time
import argparse
import tifffile
import numpy as np
import imagej.dims as dims


fetch_interval = 10
directory = Path('C:/Users/Viz4/Desktop/nate-pyimagej/MIPs')
channel_list = ['CamA_ch0']

def add_image(file_list):
    tif_list = []
    for image in sorted(file_list):
        tif_list.append(tifffile.imread(str(image)))
    print(len(tif_list))
    timelapse = np.array(tif_list)
    print(timelapse.shape)
    #(t, z, c, y, x)
    timelapse = np.reshape(timelapse, (timelapse.shape[0]//2, 1, 2, *timelapse.shape[1:]))
    print(timelapse.shape)
    return timelapse

def fetch_files():
    old_files = set()
    ui = ij.ui()
    while True:
        new_files = set()
        for cam_a, cam_b in zip(directory.glob('*CamA*.tif'), directory.glob('*CamB*.tif')):
            new_files.add(cam_a)
            new_files.add(cam_b)

        new_files.difference_update(old_files)
        old_files.update(new_files)
        try:
            dataset = ij.py.to_java(add_image(new_files))
            ui.show(dataset)
            print(ij.window().getOpenWindows())
            ij.window().clear()

        except Exception:
            time.sleep(5)




# initialize ImageJ
ij = imagej.init(mode='interactive')
ij.ui().showUI()
fetch_files()
