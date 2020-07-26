import time


def start_timer( args ):
    if args.timer:
        return time.time()
    return None

def end_timer( args, start, name ):
    if args.timer:
        print(name + " took " + str(time.time() - start) + " seconds")