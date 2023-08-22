# Purpose: Main file for the project

from antlr4 import *
from antlr4.error.ErrorStrategy import BailErrorStrategy
from gen.MyErrorListener import MyErrorListener

from gen.MyListener import MyListener
from gen.simplifiedJavaLexer import simplifiedJavaLexer
from gen.simplifiedJavaParser import simplifiedJavaParser

if __name__ == "__main__":
    data = InputStream(open("test.sjava", encoding="utf8").read())

    open("error.txt", "w").close()
    lexer = simplifiedJavaLexer(data)
    lexer.removeErrorListeners()
    lexer.addErrorListener(MyErrorListener())
    stream = CommonTokenStream(lexer)

    parser = simplifiedJavaParser(stream)
    parser.removeErrorListeners()
    parser.addErrorListener(MyErrorListener())
    tree = parser.program()

    printer = MyListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)
