#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  tax_application.py
#
#  Copyright 2018 Michel Estermann
#

import argparse
from enum import Enum


class US_StateCode(Enum):
    utah = 'UT'
    nevada = 'NV'
    texas = 'TX'
    alabama = 'AL'
    california = 'CL'

    def __str__(self):
        return self.value


taxes = {
    US_StateCode.alabama: 4.00,
    US_StateCode.california: 8.25,
    US_StateCode.nevada: 8.00,
    US_StateCode.texas: 6.25,
    US_StateCode.utah: 6.85,
}


def calculate_price(number_of_items, item_price):
    return number_of_items * item_price


def calculate_tax(price, state=US_StateCode.utah):
    return price * taxes[state] / 100.0


def parse_arguments():
    """
    Setup the argument parsers for handling CLI arguments and return a tuple
    with (parsing results, parser).
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-i",
        "--items",
        type=int,
        help='Number of items',
        action='store',
        required=True)
    parser.add_argument(
        "-p",
        "--price",
        type=float,
        help='item price',
        action='store',
        required=True)
    parser.add_argument(
        "-s",
        "--state",
        type=US_StateCode,
        default='UT',
        help='item price',
        action='store',
        choices=list(US_StateCode))

    return parser.parse_args(), parser


def main():
    """
    Main programm for the tax and order calculation programm implemented during the Elephant Carpaccio exercise
    :return:
    """
    args, parser = parse_arguments()

    order_value = calculate_price(args.items, args.price)
    tax = calculate_tax(order_value, args.state)
    print(
        "Number of items: {}. Item price: {} U$ --> Order value: {} U$".format(
            args.items, args.price, order_value))
    print("  Tax {} ({}%): {} U$".format(args.state, taxes[args.state], tax))
    print("\nTotal price: {} U$".format(order_value + tax))


if __name__ == '__main__':
    main()
