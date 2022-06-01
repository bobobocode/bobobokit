#!/usr/bin/env python3

# BoBoBo

import os


def parse_args(argv, usage):
    from argparse import ArgumentParser

    parser = ArgumentParser(prog=argv[0], usage=usage)
    opt = parser.add_argument
    opt("-p", dest="params", nargs="*", help="post parameters", default=None)
    opt("-c", dest="ini", help="config file path", default=None)

    args = parser.parse_args(argv[1:])

    if not args.ini or args.ini == "":
        s_name = argv[0].split("/")[-1].split(".")[0]
        cur = os.path.split(os.path.realpath(__file__))[0]
        args.ini = cur + "/../env/" + s_name + ".ini"
        print("Will use default config from: " + args.ini)

    return args
