import argparse

from namegenerator.formatter.formatter import Formatter
from namegenerator.formatter.abbreviated_formatter import AbbreviatedFormatter
from namegenerator.formatter.last_name_first_formatter import \
    LastNameFirstFormatter
from namegenerator.names.generator import generate_name

parser = argparse.ArgumentParser("Generate Names")
parser.add_argument('n',
                    type=int, nargs='?', default=1,
                    help='the number of names to generate')

gender = parser.add_mutually_exclusive_group()
gender.add_argument('--male',
                    dest='female', action='store_false',
                    help='generate male names')
gender.add_argument('--female',
                    dest='female', action='store_true',
                    help='generate female names (default)')

parser.add_argument('--middle-initial',
                    dest='middle_initial', action='store_true',
                    help='generate a middle initial')
parser.add_argument('--abbrev',
                    dest='abbrev', action='store_true',
                    help='print names in abbreviated form')
parser.add_argument('--last-name-first',
                    dest='last_name_first', default=False, action='store_true',
                    help='print last names first')


def main():
    args = vars(parser.parse_args())
    if args['abbrev']:
        Formatter.formatter_type = AbbreviatedFormatter
    if args['last_name_first']:
        Formatter.formatter_type = LastNameFirstFormatter
    for _ in range(args['n']):
        print(generate_name(female_name=args['female'],
                            add_middle_initial=args['middle_initial']))


if __name__ == '__main__':
    main()
