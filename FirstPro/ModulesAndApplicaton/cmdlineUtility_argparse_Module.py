""""
Using directions:

"""
import argparse
import sys
if __name__ == '__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--x',type=float,default=1.0,help='Number')
    parser.add_argument('--p',type=int,default=1,help='power to be raised')
    arg=parser.parse_args()
    sys.stdout.write(str(arg.x**arg.p))

