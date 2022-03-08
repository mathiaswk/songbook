"""
    songbook.__main__
    ~~~~~~~~~~~~~~~~~

    A one line summary of the module or program, terminated by a period.
"""

import argparse

from songbook import __version__
# from songbook.cli import cli
# from songbook.gui import gui


def _build_parser():
    parser = argparse.ArgumentParser(prog='songbook', usage='%(prog)s [options] [FILE ...]',
                        description='Create a songbook.')
    parser.add_argument('-V', '--version', action='version', version=f'%(prog)s {__version__}')
    parser.add_argument('--filelist', metavar='FILE', action='append',
                        help='reads song file names from FILE')
    parser.add_argument('--transpose', metavar='N', action='store',
                        help='Transposes by N semi-tones')

    parser.add_argument('--toc', action=argparse.BooleanOptionalAction,
                        help='generates/suppresses a table of contents')

    parser.add_argument('file', metavar='FILE', nargs='*')
    parser.add_argument(
        '-p', '--style', action='store',
        help="used for making a new pagenumber style")
    parser.add_argument(
        '-s', '--number_style', action='store',
        help="used to set the pagenumber style in the tex file")
    parser.add_argument(
        '-n', '--name', action='store',
        help="used to set the name")
    parser.add_argument(
        '-a', '--author', action='store',
        help="used to set both unf to true")
    parser.add_argument(
        '-l', '--logo', action='store',
        help="used to get a logo on the front page")
    parser.add_argument(
        '-e', '--empty', action='store',
        help="used to not have a front page")
    parser.add_argument(
        '-t', '--twosided', action='store_true')
    # TODO
    parser.add_argument('-i', '--interactive', action='store_true')
    parser.add_argument('--order', choices=['fixed', 'sorted', 'random'])
    parser.add_argument('--seed', action='store')
    return parser


def main():
    parser = _build_parser()
    args = parser.parse_args()

    # if not args.cli:
    #     cli.run()
    # else:
    #     gui.run()


if __name__ == '__main__':
    main()
