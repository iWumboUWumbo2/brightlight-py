import argparse
import sys
import math as m

parser = argparse.ArgumentParser()
g = parser.add_mutually_exclusive_group()

g.add_argument('-v', '--version', dest='version', action='store_true', help="Print program version and exit.")
g.add_argument('-p', '--percentage', dest='percent', action='store_true', help="Read the brightness level as a percentage (0 to 100) instead of the internal scale the kernel uses (such as e.g. 0 to 7812).")
g.add_argument('-r', '--read', dest='current', action='store_true', help="Read the backlight brightness level.")
g.add_argument('-w', '--write', dest='write', type=int, metavar='<val>', help="Set the backlight brightness level to <val>, where <val> is a positive integer.")
g.add_argument('-i', '--increment', '--increase', dest='increase', type=int, metavar='<val>', help="Increment/increase the backlight brightness level by <val>, where <val> is a positive integer.")
g.add_argument('-d', '--decrement', '--decrease', dest='decrease', type=int, metavar='<val>', help="Decrement/decrease the backlight brightness level by <val>, where <val> is a positive integer.")
g.add_argument('-wp', '--write-percent', dest='setpercent', type=int, metavar='<val>', help="Set the backlight brightness level to <val>%%, where <val> is a positive integer from 0 to 100.")
g.add_argument('-ip', '--inc-percent', dest='incpercent', type=int, metavar='<val>', help="Increment/increase the backlight brightness level by <val>%%, where <val> is a positive integer from 0 to 100.")
g.add_argument('-dp', '--dec-percent', dest='decpercent', type=int, metavar='<val>', help="Decrement/decrease the backlight brightness level by <val>%%, where <val> is a positive integer from 0 to 100.")
g.add_argument('-m', '--maximum', dest='max', action='store_true', help="get max brightness level of display")
parser.add_argument('-f', '--file', dest='file', type=str, default='/sys/class/backlight/intel_backlight/', metavar='<dir>', help="Specify alternative path to backlight control directory. This is likely to be a subdirectory under /sys/class/backlight/")

args = parser.parse_args()

brightness_dir = args.file
brightness_file = brightness_dir + 'brightness'
max_brightness_file = brightness_dir + 'max_brightness'

def get_current_brightness():
    f = open(brightness_file, 'r')
    brightness = f.read()
    f.close()
    return int(brightness)

def get_max_brightness():
    f = open(max_brightness_file, 'r')
    max_brightness = f.read()
    f.close()
    return int(max_brightness)

def set_brightness(value):
    ogb = get_current_brightness()
    f = open(brightness_file, 'w')
    max_b = get_max_brightness()
    value = int(value)
    strvalue = str(value) if (value <= max_b and value >= 1) else str(max_b)
    f.write(strvalue)
    f.close()
    print(f"{ogb} => {strvalue}")

def increment_brightness(delta):
    set_brightness(get_current_brightness() + delta)

def decrement_brightness(delta):
    set_brightness(get_current_brightness() - delta)

def get_brightness_percent():
    return m.floor(100 * get_current_brightness() / get_max_brightness())

def set_brightness_percent(percent):
    value = m.floor(int(percent) / 100 * get_max_brightness())
    set_brightness(value)

def increment_brightness_percent(percent):
    delta = m.floor(int(percent) / 100 * get_max_brightness())
    increment_brightness(delta)

def decrement_brightness_percent(percent):
    delta = m.floor(int(percent) / 100 * get_max_brightness())
    decrement_brightness(delta)

if (len(sys.argv) <= 1):
    print(f"Current brightness: {get_current_brightness()}")

if args.file is not None:
    brightness_dir = args.file

if args.version:
    print('brightlight-py v1\nThis program is basically a remake of brightlight in python with some quality of life improvements such as being able to set percent brightness\nIt is also less verbose which makes it great for parsing')

if args.current:
    print(get_current_brightness())

if args.max:
    print(get_max_brightness())

if args.increase is not None:
    increment_brightness(args.increase)

if args.write is not None:
    set_brightness(args.write)

if args.decrease is not None:
    decrement_brightness(args.decrease)

if args.percent:
    print(f"{get_brightness_percent()}%")

if args.setpercent is not None:
    set_brightness_percent(args.setpercent)

if args.incpercent is not None:
    increment_brightness_percent(args.incpercent)

if args.decpercent is not None:
    decrement_brightness_percent(args.decpercent)