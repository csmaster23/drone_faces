import sys
from termcolor import colored
from tello_code.base import coded_commands

def fly( args ):
    print(colored('Top of fly method', 'blue'))

    if args.fly_with_model:
        print(colored('Flying drone with face detection', 'blue'))

    else:
        print(colored('Flying drone with pre-coded commands', 'blue'))
        coded_commands( args )
