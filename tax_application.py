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


def calculate_tax(price, state):
    return price * taxes[state] / 100.0


def get_discount(price):
    if price > 50000.0:
        return 15.0
    if price > 10000.0:
        return 10.0
    if price > 7000.0:
        return 7.0
    if price > 5000.0:
        return 5.0
    if price > 1000.0:
        return 3.0
    return 0


def calculate_discounted_price(price):
    discount = get_discount(price) / 100.0
    return price * (1.0 - discount)


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
    price = calculate_discounted_price(order_value)
    price_with_tax = calculate_tax(price, args.state)
    print("Number of items: {}. Item price: {} U$".format(args.items, args.price))
    print("  Order value: {total:.2f} U$".format(total=order_value))
    print("  Order value after discount ({disc}%): {price:.2f} U$".format(disc=get_discount(order_value), price=price))
    print("  Tax {state} ({tax}%): {price:.2f} U$".format(state=args.state, tax=taxes[args.state], price=price_with_tax))
    print("\nTotal price: {0:.2f} U$".format(price + price_with_tax))


if __name__ == '__main__':
    main()
