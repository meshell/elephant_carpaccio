#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  tax_application.py
#
#  Copyright 2018 Michel Estermann
#

import argparse


def parse_arguments():
    """
    Setup the argument parsers for handling CLI arguments and return a tuple
    with (parsing results, parser).
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--items", type=int, help='Number of items', action='store', required=True)
    parser.add_argument("-p", "--price", type=float, help='item price', action='store', required=True)

    return parser.parse_args(), parser


def main():
    """
    Main programm for the tax and order calculation programm implemented during the Elephant Carpaccio exercise
    :return:
    """
    args, parser = parse_arguments()

    print("Number of items: {}. Item price: {} U$".format(args.items, args.price))
    

if __name__ == '__main__':
    main()
