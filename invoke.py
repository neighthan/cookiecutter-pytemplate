#! /usr/bin/env python

import sys
from subprocess import run

args = sys.argv[1:]
for i, arg in enumerate(args):
    if " " in arg:
        args[i] = f'"{arg}"'

run(["poetry", "run", "invoke"] + args)
