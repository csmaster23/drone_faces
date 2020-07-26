import argparse


def get_arguments():
    # PARSE ARGUMENTS
    parser = argparse.ArgumentParser()
    parser.add_argument("--run_id", type=str, help="ID used for the run", default='test01')
    parser.add_argument("--result_dir", type=str, help="path for where result directory is", default='./results')
    parser.add_argument('--batch_size', '-s', type=int, help='batch size', default=16)
    parser.add_argument('--starting_lr', '-l', type=float, help='set starting learning rate', default=0.001)
    parser.add_argument('--cpu', action="store_true", default=True)
    parser.add_argument('--gpu', action="store_true", default=False)
    parser.add_argument('--fly_tello', action="store_true", default=False)
    parser.add_argument('--fly_with_model', action="store_true", default=False)
    parser.add_argument('--fly_basic', action="store_true", default=False)
    parser.add_argument('--camera_only', action="store_true", default=True)
    parser.add_argument('--stream_camera', action="store_true", default=True)
    parser.add_argument('--command_num', type=int, help='number of times to re-execute a command for basic flight', default=3)
    parser.add_argument('--drone_command_max_time_out', type=int, help='seconds to wait for command', default=5)
    parser.add_argument('--train_model', action="store_true", default=False)
    parser.add_argument('--load_images', action="store_true", default=True)
    parser.add_argument("--image_dir", type=str, help="path for where the images to load are", default='./img')
    parser.add_argument("--save_dir", type=str, help="path for where the images are saved to", default='./save_pictures')
    parser.add_argument('--save_images', action="store_true", default=False)
    parser.add_argument('--resize_images', action="store_true", default=False)
    parser.add_argument('--resize_size', type=int, help='square size to resize', default=200)
    parser.add_argument('--num_pics', type=int, help='num pictures to load', default=5)
    parser.add_argument('--timer', action="store_true", default=True)



    args = parser.parse_args()

    return args
