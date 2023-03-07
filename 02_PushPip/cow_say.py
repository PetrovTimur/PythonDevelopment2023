import argparse
import cowsay

parser = argparse.ArgumentParser()
parser.add_argument('message', help='message the cow says', nargs='?')
parser.add_argument('-e', help='specify the look of eyes', type=str, default='oo')
parser.add_argument('-f', help='specify a particular cow picture file to use', type=str)
parser.add_argument('-l', help='list all cowfiles on the current COWPATH', action='store_true')
parser.add_argument('-n', help='turn off word-wrapping', action='store_true')
parser.add_argument('-T', help='specify tongue string', type=str, default='')
parser.add_argument('-W', help='width of the text bubble', type=int)

args = parser.parse_args()

if args.l:
    print(*cowsay.list_cows())
else:
    print(cowsay.cowsay(message=args.message, eyes=args.e, tongue=args.T, width=args.W, wrap_text=args.n, cowfile=args.f))