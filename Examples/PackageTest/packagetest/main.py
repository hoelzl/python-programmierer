import argparse

from packagetest.formatter.formatter import Formatter
from packagetest.formatter.abbreviated_formatter import AbbreviatedFormatter
from packagetest.formatter.last_name_first_formatter import \
    LastNameFirstFormatter
from packagetest.names.generator import generate_name

parser = argparse.ArgumentParser("Generate Names")
parser.add_argument('n',
                    type=int, nargs='?', default=1,
                    help='the number of names to generate')
parser.add_argument('--female',
                    dest='female', default=True, action='store_true',
                    help='generate female names (default)')
parser.add_argument('--male',
                    dest='female', action='store_false',
                    help='generate male names')
parser.add_argument('--middle-initial',
                    dest='middle_initial', default=False, action='store_true',
                    help='generate a middle initial')
parser.add_argument('--abbrev',
                    dest='abbrev', default=False, action='store_true',
                    help='print names in abbreviated form')
parser.add_argument('--last-name-first',
                    dest='last_name_first', default=False, action='store_true',
                    help='print last names first')

if __name__ == '__main__':
    args = vars(parser.parse_args())
    if args['abbrev']:
        Formatter.formatter_type = AbbreviatedFormatter
    if args['last_name_first']:
        Formatter.formatter_type = LastNameFirstFormatter
    for _ in range(args['n']):
        print(generate_name(female_name=args['female'],
                            add_middle_initial=args['middle_initial']))
