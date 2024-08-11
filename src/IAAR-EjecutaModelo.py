# ======================================================================================
# CARLOS GARCIA SILVA - 2021
# ======================================================================================
# Universidad de Huelva
# Ingenieria Informatica - Computacion
# Inteligencia aplicada a Robots
# ======================================================================================

import jetson.inference
import jetson.utils

import argparse
import sys

# ======================================================================================
# Parse the command line
# ======================================================================================
parser = argparse.ArgumentParser(description = "Locate objects in a live camera stream using an object detection DNN.", 
            formatter_class = argparse.RawTextHelpFormatter, epilog=jetson.inference.detectNet.Usage()
                + jetson.utils.videoSource.Usage() 
                + jetson.utils.videoOutput.Usage() 
                + jetson.utils.logUsage())

parser.add_argument("input_URI", type = str, default = "", nargs = '?', help = "URI of the input stream")
parser.add_argument("output_URI", type = str, default = "", nargs = '?', help = "URI of the output stream")
parser.add_argument("--network", type = str, default = "ssd-mobilenet-v2", help = "pre-trained model to load (see below for options)")
parser.add_argument("--overlay", type = str, default = "box,labels,conf", help = "detection overlay flags (e.g. --overlay=box,labels,conf)\nvalid combinations are:  'box', 'labels', 'conf', 'none'")
parser.add_argument("--threshold", type = float, default = 0.5, help = "minimum detection threshold to use") 

is_headless = ["--headless"] if sys.argv[0].find('console.py') != -1 else [""]

try:
	opt = parser.parse_known_args()[0]
except:
	print("")
	parser.print_help()
	sys.exit(0)

# ======================================================================================
# Load the object detection network
# ======================================================================================
argv=['--model=/home/alumno2/Desktop/IAAR/Deteccion-objetos/jetson-inference/python/training/detection/ssd/models/faces25/ssd-mobilenet.onnx',
	'--labels=/home/alumno2/Desktop/IAAR/Deteccion-objetos/jetson-inference/python/training/detection/ssd/models/faces25/labels.txt',
	'--input-blob=input_0',
	'--output-cvg=scores',
	'--output-bbox=boxes']

net = jetson.inference.detectNet("SDD-IAAR", argv, threshold=.5)

# ======================================================================================
# create video sources & outputs
# ======================================================================================
input = jetson.utils.videoSource("csi://0", argv=['--input-flip=rotate-180'])
output = jetson.utils.videoOutput(opt.output_URI, argv=sys.argv+is_headless)

# ======================================================================================
# process frames until the user exits
# ======================================================================================
while True:
	# capture the next image
	img = input.Capture()

	# detect objects in the image (with overlay)
	detections = net.Detect(img, overlay=opt.overlay)

	# print the detections
	print("detected {:d} objects in image".format(len(detections)))

	for detection in detections:
		print(detection)

	# render the image
	output.Render(img)

	# update the title bar
	output.SetStatus("{:s} | Network {:.0f} FPS".format("Modelo para personas", net.GetNetworkFPS()))

	# print out performance info
	net.PrintProfilerTimes()

	# exit on input/output EOS
	if not input.IsStreaming() or not output.IsStreaming():
		break