import sys
import time
import argparse
from zutils import monitor

parser = argparse.ArgumentParser()
parser.add_argument("--interface", "--proxy",
                    "--device", nargs="+", default="*")
parser.add_argument("--xin", "--in_bound", default="5555")
parser.add_argument("--xout", "--out_bound", default="5556")
args = parser.parse_args()

interface = args.interface
xin = args.xin
xout = args.xout

monitor(interface, xin, xout)
