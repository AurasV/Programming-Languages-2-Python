import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--a", type=float, required=True)
parser.add_argument("--b", type=float, required=True)
parser.add_argument("--op", choices=["+", "-", "/", "*", "mean"], required=True)

args = parser.parse_args()

match args.op:
    case "+":
        print(args.a + args.b)
    case "-":
        print(args.a - args.b)
    case "/":
        print(args.a / args.b)
    case "*":
        print(args.a * args.b)
    case "mean":
        print((args.a + args.b) / 2)
