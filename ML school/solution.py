from functions import *
import logging
from argparse import ArgumentParser



if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument("--path", type=str, nargs=1, metavar="PATH",
                        default=None, help="folder with images")
    args = parser.parse_args()
    if args.path:
        path_processing(args)
    else:
        logger.debug("error: the following arguments are required: --path")