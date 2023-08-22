from antlr4.error.ErrorListener import ErrorListener as BaseErrorListener

class MyErrorListener(BaseErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print(f"line {line}:{column} {msg}", file=open("error.txt", "a"))
