import os

from antlr4 import *

from gen.MyListener import MyListener
from gen.simplifiedJavaLexer import simplifiedJavaLexer
from gen.simplifiedJavaParser import simplifiedJavaParser

if __name__ == "__main__":
    data = InputStream(open("test.sjava", encoding="utf8").read())

    lexer = simplifiedJavaLexer(data)
    stream = CommonTokenStream(lexer)

    parser = simplifiedJavaParser(stream)
    tree = parser.program()

    printer = MyListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)
