from glob import glob
import imagej, time, argparse
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument('directory', type=str)
parser.add_argument('channels', type=str)
parser.add_argument('--opacity', type=float, nargs='+', default=[1.0],
    help='Space seperated floats (0.0-1.0) for each channel. --opacity 1.0 1.0')          
parser.add_argument('--contrast_limits', type=float, nargs='+', default=[None],
    help='Two space seperated floats for each channel. --contrast_limits 0.0 100.0 0.0 100.0')   
parser.add_argument('--gamma', type=float, nargs='+', default=[1.0], 
    help='Space seperated floats (0.0-2.0) for each channel. --gamma 1.0 1.0')             
parser.add_argument('--colormaps', type=str, default='blue,green,red,magenta,yellow,orange,cyan',
    help='Comma seperated string with colormap for each channel. --colormaps blue,green')    
parser.add_argument('--blending', type=str, default='additive', 
    help='Single string for blending method. --blending additive')       
parser.add_argument('--interpolation', type=str, default='nearest',
    help='Single string for interpolation method. --interpolation nearest')                                        
parser.add_argument('--fetch_interval', type=int, default=10, 
    help='Duration to wait between checking folder for new files (seconds)')
parser.add_argument('--layer_buffer', type=int, default=2, 
    help='Amount of layers to leave out when processing new files')       
args = parser.parse_args()  

# ij = imagej.init('sc.fiji:fiji:2.3.1')
channel_list = args.channels.split(',')

def fetch_files():
    old_files = []
    while True:
        new_files = []
        
        for file in sorted(glob(args.directory+'/*tif'))[: -args.layer_buffer or None]:
            if file not in old_files:
                new_files.append(file)
                old_files.append(file)

        for channel in channel_list:
            file_list = []
            for file in new_files:
                if channel in file:
                    file_list.append(file)
            yield file_list
        time.sleep(args.fetch_interval)

for file in fetch_files():
    print(file)