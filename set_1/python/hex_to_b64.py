#!/usr/bin/env python3
# PSEUDOCODE
# Convert hex to binary format.
# Convert binary to decimal.
# Use chr(dec_str) to convert into ASCII.
# Chunk it and base64-encode the ASCII text.

import math


def hex_to_bin(hex_str):
    hex_int = int(hex_str, 16)
    bin_str = ''
    while hex_int > 0:
        bin_str += str(hex_int % 2)
        hex_int = hex_int >> 1
    return bin_str


def bin_to_dec(bin_str):
    dec_val = 0
    for i in range(len(bin_str) - 1, -1, -1):
        if bin_str[i] == "1":
            dec_val += int(math.pow(2, i))
    return dec_val


def main():
    hex_str = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
    bin_str = hex_to_bin(hex_str)
    # Pad the number of chars until divisible by 6.
    while not(len(bin_str) % 6 == 0):
        bin_str += "0"
    b64_str = ''
    for i in range(0, len(bin_str) - 6):
        b64_str += chr(bin_to_dec(bin_str[i:i+6]))
    print(b64_str)


if __name__ == "__main__":
    main()
