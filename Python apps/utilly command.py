
# import argparse
# import sys
    
# def calc(args):
#     if args.o == 'add':
#         return args.x + args.y

#     elif args.o == 'mul':
#         return args.x * args.y

#     elif args.o == 'sub':
#         return args.x - args.y

#     elif args.o == 'div':
#         return args.x / args.y

#     else:
#         return "Something went wrong"

# if __name__ == '__main__':
#     parser = argparse.ArgumentParser()
#     parser.add_argument('--x', type=float, default=1.0,
#                         help="Enter first number. This is a utility for calculation. Please contact harry bhai")

#     parser.add_argument('--y', type=float, default=3.0,
#                         help="Enter second number. This is a utility for calculation. Please contact harry bhai")

#     parser.add_argument('--o', type=str, default="add",
#                         help="This is a utility for calculation. Please contact harry bhai for more")

#     args = parser.parse_args()
#     sys.stdout.write(str(calc(args)))
def calc(args):
    if args.o=='add':
        return args.a + args.b
    
    elif args.o=='sub':
        return args.a - args.b
    
    elif args.o=='mul':
        return args.a * args.b
    
    elif args.o=='div':
        return args.a / args.b
    elif args.a==45 and args.b==3 and args.o=='mul':
        return 555
    
    elif args.a==56 and args.b==9 and args.o=='add':
        return 77
    
    elif args.a==56 and args.b==6 and args.o=='div':
        return 44
import argparse
import sys
if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--a", type=float, default=1.0,
                        help="Enter First number:")
    parser.add_argument("--b", type=float, default=1.0,
                        help="Enter second number:")
    parser.add_argument("--o", type=str, default='add',
                        help="We will help you.")
    args = parser.parse_args()
    sys.stdout.write(str(calc(args)))