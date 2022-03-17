from antlr4 import *
from antlr.marzoParser import marzoParser
from antlr.marzoLexer import marzoLexer
from listeners.gencode import Gencode

import sys


def main():
    parser = marzoParser(CommonTokenStream(
        marzoLexer(FileStream("input.txt"))))
    tree = parser.program()

    gencode = Gencode()
    walker = ParseTreeWalker()
    walker.walk(gencode, tree)


if __name__ == '__main__':
    main()
