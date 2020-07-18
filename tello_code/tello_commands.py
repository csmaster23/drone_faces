import sys
import cv2
from termcolor import colored
from easytello import tello

# Tello Info dict_keys(['local_ip', 'local_port', 'socket', 'tello_ip', 'tello_port', 'tello_address', 'log', 'receive_thread', 'stream_state', 'MAX_TIME_OUT', 'debug'])

def connect( args ):
	print(colored('Connecting to tello...', 'blue'))

	drone = tello.Tello()
	if args.stream_camera:
		drone.streamon()
	drone.MAX_TIME_OUT = args.drone_command_max_time_out

	print(colored('Successful tello connection', 'blue'))
	return drone

