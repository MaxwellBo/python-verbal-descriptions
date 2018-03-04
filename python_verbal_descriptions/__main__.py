import argparse

from .py_ast import verbalise_code

SRC_TYPE_FILE = 'file'
SRC_TYPE_TEXT = 'text'

def main():
    parser = argparse.ArgumentParser(
        description='Generate English verbal descriptions for Python'
    )
    parser.add_argument(
        '--type', '-t',
        dest='src_type',
        action='store',
        choices=(SRC_TYPE_FILE, SRC_TYPE_TEXT),
        default=SRC_TYPE_TEXT,
        help='source type (defaults to text)'
    )
    parser.add_argument(
        '--src', '-s',
        dest='src',
        action='store',
        required=True,
        help='source'
    )

    args = parser.parse_args()

    if args.src_type == SRC_TYPE_FILE:
        with open(args.src, 'r') as f:
            raw_src = f.read()
    else:
        raw_src = args.src

    print(verbalise_code(raw_src))

if __name__ == '__main__':
    main()
