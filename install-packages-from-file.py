#!/usr/bin/env python
from sys import argv
from os import system
if len(argv) < 2:
    print("Usage: " + argv[0] + " <file>")
    exit()

path = argv[1]
fi = open(path, "r")
exec_str = "pacman --noconfirm -S "
for line in fi:
    line = line.strip()
    exec_str += line + " "
fi.close()

system(exec_str)
