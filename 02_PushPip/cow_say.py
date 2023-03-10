import argparse
import cowsay

parser = argparse.ArgumentParser()
parser.add_argument('message', help='message the cow says', nargs='?')
parser.add_argument('-e', help='specify the look of eyes', type=str, default='oo', metavar='eyes')
parser.add_argument('-f', help='specify a particular cow picture file to use', type=str, metavar='cowfile')
parser.add_argument('-l', help='list all cowfiles on the current COWPATH', action='store_true')
parser.add_argument('-n', help='turn off word-wrapping', action='store_true')
parser.add_argument('-T', help='specify tongue string', type=str, default='', metavar='tongue')
parser.add_argument('-W', help='width of the text bubble', type=int, default=40, metavar='wrapcolumn')
parser.add_argument('-b', help='Borg mode', action='store_true')
parser.add_argument('-d', help='dead mode', action='store_true')
parser.add_argument('-g', help='greedy mode', action='store_true')
parser.add_argument('-p', help='paranoia mode', action='store_true')
parser.add_argument('-s', help='stoned mode', action='store_true')
parser.add_argument('-t', help='tired mode', action='store_true')
parser.add_argument('-w', help='wired mode', action='store_true')
parser.add_argument('-y', help='youthful mode', action='store_true')

args = parser.parse_args()

if args.l:
    print(*cowsay.list_cows())
else:
    mask = 'bdgpstwy'
    options = ''.join([c for c in mask if args.__dict__[c]])

    print(cowsay.cowsay(message=args.message, eyes=args.e, tongue=args.T, width=args.W, wrap_text=args.n, cowfile=args.f, preset=options))
