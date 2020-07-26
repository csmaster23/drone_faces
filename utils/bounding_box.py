import cv2
import dlib
import time
from termcolor import colored
from utils.util import start_timer, end_timer


def load_images( args ):
    print(colored("Loading Images from " + str(args.image_dir) + "...", 'green'))

    imgs = [ cv2.imread( args.image_dir + "/picture_" + str(i) + ".png") for i in range(args.num_pics) ]
    print("Length of imgs: %s" % str(len(imgs)))

    print(colored("Draw Bounding Boxes...", 'blue'))

    detector = dlib.get_frontal_face_detector()

    counter = 0
    for img in imgs:
        start = start_timer( args )
        rect_img = find_face( img, detector, args, counter )
        end_timer( args, start, "Face dection" )
        counter += 1


def find_face( img, detector, args, id ):
    if args.resize_images:
        img = cv2.resize( img, (args.resize_size, args.resize_size))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector(gray, 1)  # result
    # to draw faces on image
    for result in faces:
        x = result.left()
        y = result.top()
        x1 = result.right()
        y1 = result.bottom()
        img = cv2.rectangle(img, (x, y), (x1, y1), (0, 0, 255), 2)
    if args.save_images:
        cv2.imwrite(args.save_dir + "/rect_" + str(id) + ".png", img)
    return img

