# Tanner Norton - Tello Project - Started October 2019

# imports
import sys
import time
from termcolor import colored
# from tello_code.tello_main import fly
from utils.arguments import get_arguments
from utils.start_helpers import print_args
from utils.bounding_box import find_face, load_images

def main():
	print(colored('Drone Faces Main', 'blue'))

	print(colored('Gather Arguments...', 'blue'))
	args = get_arguments()
	print_args( args )

	### Load a trained model and fly the drone ###
	if args.fly_tello:
		pass
		# fly( args )

	elif args.train_model:
		pass

	elif args.load_images:
		load_images( args )




	print(colored('Whole Program has finished gracefully.', 'blue'))

if __name__ == "__main__":
	main()
