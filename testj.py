import imagej

# initialize ImageJ
ij = imagej.init('sc.fiji:fiji:2.1.1')	
print("ImageJ version: {ij.getVersion()}")