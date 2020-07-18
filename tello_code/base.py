import cv2
import time
from termcolor import colored
from tello_code.tello_commands import connect


def coded_commands( args ):
    if args.fly_basic:
        basic_flight( args )
    elif args.camera_only:
        camera_stream( args )



def camera_stream( args ):
    # Connect to tello
    drone = connect( args )
    time.sleep(3)
    drone.streamoff()
    print(colored('Drone camera stream off.', 'red'))


def basic_flight( args ):
    # Connect to tello
    drone = connect( args )

    # Begin Flight
    time.sleep(2)
    drone.takeoff()
    time.sleep(2)

    # Rotate 360 degrees
    for i in range( args.command_num ):
        drone.cw(360)
        time.sleep(2)

    # Land
    drone.land()
    print(colored('Drone has landed.', 'blue'))
