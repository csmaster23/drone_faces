import sys


### Print All Arguments ###
def print_args( args ):
    print("Arguments:")
    print("{:<50} {:<25}".format('Key:', 'Value:'))
    for arg in vars(args):
        print("{:<50} {:<25}".format(str(arg), str(getattr(args,arg))))
    print()
