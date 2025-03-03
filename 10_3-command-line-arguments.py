import sys
import argparse
print(sys.argv)

parser = argparse.ArgumentParser(
    prog='top',
    description='Show top lines from each file')
parser.add_argument('filenames', nargs='+')
parser.add_argument('-1', '--lines', type=int, default=10)
args = parser.parse_args()
print(args)
