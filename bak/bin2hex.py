#!/usr/bin/env python

import sys
import binascii

# byte_per_line = 4
byte_per_line = 1

with open(sys.argv[1], 'rb') as f:
  str_bin = binascii.hexlify(f.read())
  ls_byte = [str_bin[i:i+2] for i in range(0, len(str_bin), 2)]
  # ls_qword = [''.join(list(reversed(ls_byte[i:i+4]))) for i in range(0, len(ls_byte), 4)]
  ls_line = [''.join(list(reversed(ls_byte[i:i+byte_per_line]))) for i in range(0, len(ls_byte), byte_per_line)]

  for line in ls_line:
    print(line)
