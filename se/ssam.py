#!/usr/bin/env python3

"""
usage: ssam [-n] <script> [ <file> ... ]
"""

from pathlib import Path

import docopt

from se import call, parse


def ssam(expr, string, echo_input=True):
    selections = ""
    if expr:
        string, selections = call(parse(expr), string)
    if selections:
        print("".join(map(str, selections)), end="")
    if echo_input:
        print(string, end="")


def main(argv=None):
    args = docopt(__doc__, argv)
    for f in files:
        text = Path(f).read_text()
        ssam(args["script"], text, echo_input=args["-n"])


if __name__ == "__main__":
    main()
