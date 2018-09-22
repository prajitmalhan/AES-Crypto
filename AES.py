#!/usr/bin/env python3

import argparse

# Handles the command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument('--keysize', type=int, required=True)
parser.add_argument('--keyfile', type=argparse.FileType('r'), required=True)
parser.add_argument('--inputfile', type=argparse.FileType('r'), required=True)
parser.add_argument('--outputfile', type=argparse.FileType('w'), required=True)
parser.add_argument('--mode', type=str, required=True)
args = parser.parse_args()

# Function to handle key expansion step
def key_expansion() :
    # TO-DO

# Function to handle the entire initial round
def initial_round() :
    # TO-DO

# Function to handle the subByte step
def sub_bytes() :
    # TO-DO

# Function that handles shifting row step
def shift_rows() :
    # TO-DO

# Function to handle mixing columns step
def mix_columns() :
    # TO-DO

# Function to handle add round key step
def add_round_key() :
    # TO-DO

# Encryption skeleton
def encrypt() :
    num_rounds = n

    key_expansion()
    initial_round()

    for i in range(0, num_rounds) :
        sub_bytes()
        shift_rows()
        mix_columns()
        add_round_key()

    # Final Round
    sub_bytes()
    shift_rows()
    add_round_key()
