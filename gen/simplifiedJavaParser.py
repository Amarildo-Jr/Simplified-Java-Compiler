# Generated from C:/Repositórios/Projetos/UFPI/Compiladores/Simplified-Java-Compiler\simplifiedJava.g4 by ANTLR 4.12.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,41,252,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,1,0,3,0,48,8,0,1,0,1,0,1,0,1,1,4,1,54,8,
        1,11,1,12,1,55,1,2,1,2,3,2,60,8,2,1,2,3,2,63,8,2,1,2,1,2,1,3,1,3,
        1,3,3,3,70,8,3,1,3,1,3,1,3,1,3,3,3,76,8,3,1,4,1,4,1,4,1,4,1,4,1,
        4,5,4,84,8,4,10,4,12,4,87,9,4,1,5,1,5,1,5,3,5,92,8,5,1,5,3,5,95,
        8,5,1,5,1,5,1,6,1,6,1,6,4,6,102,8,6,11,6,12,6,103,1,7,1,7,1,7,1,
        7,1,7,1,7,1,7,1,7,1,7,3,7,115,8,7,1,8,4,8,118,8,8,11,8,12,8,119,
        1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,
        3,9,138,8,9,1,10,1,10,3,10,142,8,10,1,11,1,11,1,11,1,11,1,11,1,11,
        3,11,150,8,11,1,11,3,11,153,8,11,1,11,1,11,1,12,1,12,1,12,3,12,160,
        8,12,1,13,1,13,1,13,1,13,1,13,1,13,3,13,168,8,13,1,13,1,13,1,14,
        1,14,1,14,5,14,175,8,14,10,14,12,14,178,9,14,1,15,1,15,1,15,1,15,
        1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,3,16,194,8,16,
        1,17,1,17,1,17,5,17,199,8,17,10,17,12,17,202,9,17,1,18,1,18,1,18,
        1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,3,18,216,8,18,1,18,
        1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,5,18,230,
        8,18,10,18,12,18,233,9,18,1,19,1,19,1,19,3,19,238,8,19,1,19,1,19,
        1,20,1,20,1,20,1,20,3,20,246,8,20,1,21,1,21,1,22,1,22,1,22,0,1,36,
        23,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,
        44,0,6,1,0,21,22,2,0,20,20,23,23,1,0,24,27,1,0,28,29,1,0,30,33,1,
        0,34,37,264,0,47,1,0,0,0,2,53,1,0,0,0,4,57,1,0,0,0,6,66,1,0,0,0,
        8,77,1,0,0,0,10,88,1,0,0,0,12,98,1,0,0,0,14,114,1,0,0,0,16,117,1,
        0,0,0,18,137,1,0,0,0,20,141,1,0,0,0,22,143,1,0,0,0,24,156,1,0,0,
        0,26,161,1,0,0,0,28,171,1,0,0,0,30,179,1,0,0,0,32,193,1,0,0,0,34,
        195,1,0,0,0,36,215,1,0,0,0,38,234,1,0,0,0,40,245,1,0,0,0,42,247,
        1,0,0,0,44,249,1,0,0,0,46,48,3,2,1,0,47,46,1,0,0,0,47,48,1,0,0,0,
        48,49,1,0,0,0,49,50,3,10,5,0,50,51,5,0,0,1,51,1,1,0,0,0,52,54,3,
        4,2,0,53,52,1,0,0,0,54,55,1,0,0,0,55,53,1,0,0,0,55,56,1,0,0,0,56,
        3,1,0,0,0,57,59,3,6,3,0,58,60,3,12,6,0,59,58,1,0,0,0,59,60,1,0,0,
        0,60,62,1,0,0,0,61,63,3,16,8,0,62,61,1,0,0,0,62,63,1,0,0,0,63,64,
        1,0,0,0,64,65,5,1,0,0,65,5,1,0,0,0,66,67,5,38,0,0,67,69,5,2,0,0,
        68,70,3,8,4,0,69,68,1,0,0,0,69,70,1,0,0,0,70,71,1,0,0,0,71,72,5,
        3,0,0,72,75,5,4,0,0,73,76,3,42,21,0,74,76,5,5,0,0,75,73,1,0,0,0,
        75,74,1,0,0,0,76,7,1,0,0,0,77,78,3,42,21,0,78,85,5,38,0,0,79,80,
        5,6,0,0,80,81,3,42,21,0,81,82,5,38,0,0,82,84,1,0,0,0,83,79,1,0,0,
        0,84,87,1,0,0,0,85,83,1,0,0,0,85,86,1,0,0,0,86,9,1,0,0,0,87,85,1,
        0,0,0,88,89,5,7,0,0,89,91,5,4,0,0,90,92,3,12,6,0,91,90,1,0,0,0,91,
        92,1,0,0,0,92,94,1,0,0,0,93,95,3,16,8,0,94,93,1,0,0,0,94,95,1,0,
        0,0,95,96,1,0,0,0,96,97,5,1,0,0,97,11,1,0,0,0,98,99,5,8,0,0,99,101,
        5,4,0,0,100,102,3,14,7,0,101,100,1,0,0,0,102,103,1,0,0,0,103,101,
        1,0,0,0,103,104,1,0,0,0,104,13,1,0,0,0,105,106,3,40,20,0,106,107,
        5,4,0,0,107,108,3,42,21,0,108,109,5,9,0,0,109,115,1,0,0,0,110,111,
        5,10,0,0,111,112,3,28,14,0,112,113,5,9,0,0,113,115,1,0,0,0,114,105,
        1,0,0,0,114,110,1,0,0,0,115,15,1,0,0,0,116,118,3,18,9,0,117,116,
        1,0,0,0,118,119,1,0,0,0,119,117,1,0,0,0,119,120,1,0,0,0,120,17,1,
        0,0,0,121,138,3,20,10,0,122,123,3,30,15,0,123,124,5,9,0,0,124,138,
        1,0,0,0,125,126,3,32,16,0,126,127,5,9,0,0,127,138,1,0,0,0,128,129,
        3,38,19,0,129,130,5,9,0,0,130,138,1,0,0,0,131,132,5,11,0,0,132,133,
        3,36,18,0,133,134,5,9,0,0,134,138,1,0,0,0,135,136,5,12,0,0,136,138,
        5,9,0,0,137,121,1,0,0,0,137,122,1,0,0,0,137,125,1,0,0,0,137,128,
        1,0,0,0,137,131,1,0,0,0,137,135,1,0,0,0,138,19,1,0,0,0,139,142,3,
        22,11,0,140,142,3,26,13,0,141,139,1,0,0,0,141,140,1,0,0,0,142,21,
        1,0,0,0,143,144,5,13,0,0,144,145,5,2,0,0,145,146,3,36,18,0,146,147,
        5,3,0,0,147,149,5,4,0,0,148,150,3,16,8,0,149,148,1,0,0,0,149,150,
        1,0,0,0,150,152,1,0,0,0,151,153,3,24,12,0,152,151,1,0,0,0,152,153,
        1,0,0,0,153,154,1,0,0,0,154,155,5,1,0,0,155,23,1,0,0,0,156,157,5,
        14,0,0,157,159,5,4,0,0,158,160,3,16,8,0,159,158,1,0,0,0,159,160,
        1,0,0,0,160,25,1,0,0,0,161,162,5,15,0,0,162,163,5,2,0,0,163,164,
        3,36,18,0,164,165,5,3,0,0,165,167,5,4,0,0,166,168,3,16,8,0,167,166,
        1,0,0,0,167,168,1,0,0,0,168,169,1,0,0,0,169,170,5,1,0,0,170,27,1,
        0,0,0,171,176,3,30,15,0,172,173,5,6,0,0,173,175,3,30,15,0,174,172,
        1,0,0,0,175,178,1,0,0,0,176,174,1,0,0,0,176,177,1,0,0,0,177,29,1,
        0,0,0,178,176,1,0,0,0,179,180,5,38,0,0,180,181,5,16,0,0,181,182,
        3,36,18,0,182,31,1,0,0,0,183,184,5,17,0,0,184,185,5,2,0,0,185,186,
        3,34,17,0,186,187,5,3,0,0,187,194,1,0,0,0,188,189,5,18,0,0,189,190,
        5,2,0,0,190,191,3,40,20,0,191,192,5,3,0,0,192,194,1,0,0,0,193,183,
        1,0,0,0,193,188,1,0,0,0,194,33,1,0,0,0,195,200,3,36,18,0,196,197,
        5,6,0,0,197,199,3,36,18,0,198,196,1,0,0,0,199,202,1,0,0,0,200,198,
        1,0,0,0,200,201,1,0,0,0,201,35,1,0,0,0,202,200,1,0,0,0,203,204,6,
        18,-1,0,204,205,5,2,0,0,205,206,3,36,18,0,206,207,5,3,0,0,207,216,
        1,0,0,0,208,209,5,19,0,0,209,216,3,36,18,9,210,211,5,20,0,0,211,
        216,3,36,18,8,212,216,3,38,19,0,213,216,3,44,22,0,214,216,5,38,0,
        0,215,203,1,0,0,0,215,208,1,0,0,0,215,210,1,0,0,0,215,212,1,0,0,
        0,215,213,1,0,0,0,215,214,1,0,0,0,216,231,1,0,0,0,217,218,10,7,0,
        0,218,219,7,0,0,0,219,230,3,36,18,8,220,221,10,6,0,0,221,222,7,1,
        0,0,222,230,3,36,18,7,223,224,10,5,0,0,224,225,7,2,0,0,225,230,3,
        36,18,6,226,227,10,4,0,0,227,228,7,3,0,0,228,230,3,36,18,5,229,217,
        1,0,0,0,229,220,1,0,0,0,229,223,1,0,0,0,229,226,1,0,0,0,230,233,
        1,0,0,0,231,229,1,0,0,0,231,232,1,0,0,0,232,37,1,0,0,0,233,231,1,
        0,0,0,234,235,5,38,0,0,235,237,5,2,0,0,236,238,3,34,17,0,237,236,
        1,0,0,0,237,238,1,0,0,0,238,239,1,0,0,0,239,240,5,3,0,0,240,39,1,
        0,0,0,241,246,5,38,0,0,242,243,5,38,0,0,243,244,5,6,0,0,244,246,
        3,40,20,0,245,241,1,0,0,0,245,242,1,0,0,0,246,41,1,0,0,0,247,248,
        7,4,0,0,248,43,1,0,0,0,249,250,7,5,0,0,250,45,1,0,0,0,26,47,55,59,
        62,69,75,85,91,94,103,114,119,137,141,149,152,159,167,176,193,200,
        215,229,231,237,245
    ]

class simplifiedJavaParser ( Parser ):

    grammarFileName = "simplifiedJava.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'end'", "'('", "')'", "':'", "'void'", 
                     "','", "'main'", "'var'", "';'", "'const'", "'return'", 
                     "'break'", "'if'", "'else'", "'while'", "'='", "'print'", 
                     "'scanf'", "'!'", "'-'", "'*'", "'/'", "'+'", "'<'", 
                     "'>'", "'<='", "'>='", "'=='", "'!='", "'int'", "'float'", 
                     "'str'", "'bool'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "INT", "FLOAT", "STRING", 
                      "BOOL", "ID", "OneLineComment", "MultiLineComment", 
                      "WS" ]

    RULE_program = 0
    RULE_functionsBlock = 1
    RULE_function = 2
    RULE_functionDeclaration = 3
    RULE_declarationParametersList = 4
    RULE_mainFunction = 5
    RULE_variableDeclarationArea = 6
    RULE_variableDeclaration = 7
    RULE_cmdBlock = 8
    RULE_command = 9
    RULE_controlCmd = 10
    RULE_ifCmd = 11
    RULE_elseCmd = 12
    RULE_whileCmd = 13
    RULE_attributionList = 14
    RULE_attributionCmd = 15
    RULE_ioCmd = 16
    RULE_expressionList = 17
    RULE_expression = 18
    RULE_functionCall = 19
    RULE_variableList = 20
    RULE_type = 21
    RULE_literal = 22

    ruleNames =  [ "program", "functionsBlock", "function", "functionDeclaration", 
                   "declarationParametersList", "mainFunction", "variableDeclarationArea", 
                   "variableDeclaration", "cmdBlock", "command", "controlCmd", 
                   "ifCmd", "elseCmd", "whileCmd", "attributionList", "attributionCmd", 
                   "ioCmd", "expressionList", "expression", "functionCall", 
                   "variableList", "type", "literal" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    T__31=32
    T__32=33
    INT=34
    FLOAT=35
    STRING=36
    BOOL=37
    ID=38
    OneLineComment=39
    MultiLineComment=40
    WS=41

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.12.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mainFunction(self):
            return self.getTypedRuleContext(simplifiedJavaParser.MainFunctionContext,0)


        def EOF(self):
            return self.getToken(simplifiedJavaParser.EOF, 0)

        def functionsBlock(self):
            return self.getTypedRuleContext(simplifiedJavaParser.FunctionsBlockContext,0)


        def getRuleIndex(self):
            return simplifiedJavaParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = simplifiedJavaParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==38:
                self.state = 46
                self.functionsBlock()


            self.state = 49
            self.mainFunction()
            self.state = 50
            self.match(simplifiedJavaParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionsBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(simplifiedJavaParser.FunctionContext)
            else:
                return self.getTypedRuleContext(simplifiedJavaParser.FunctionContext,i)


        def getRuleIndex(self):
            return simplifiedJavaParser.RULE_functionsBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionsBlock" ):
                listener.enterFunctionsBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionsBlock" ):
                listener.exitFunctionsBlock(self)




    def functionsBlock(self):

        localctx = simplifiedJavaParser.FunctionsBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_functionsBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 52
                self.function()
                self.state = 55 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==38):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def functionDeclaration(self):
            return self.getTypedRuleContext(simplifiedJavaParser.FunctionDeclarationContext,0)


        def variableDeclarationArea(self):
            return self.getTypedRuleContext(simplifiedJavaParser.VariableDeclarationAreaContext,0)


        def cmdBlock(self):
            return self.getTypedRuleContext(simplifiedJavaParser.CmdBlockContext,0)


        def getRuleIndex(self):
            return simplifiedJavaParser.RULE_function

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction" ):
                listener.enterFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction" ):
                listener.exitFunction(self)




    def function(self):

        localctx = simplifiedJavaParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_function)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.functionDeclaration()
            self.state = 59
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==8:
                self.state = 58
                self.variableDeclarationArea()


            self.state = 62
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 274878347264) != 0):
                self.state = 61
                self.cmdBlock()


            self.state = 64
            self.match(simplifiedJavaParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(simplifiedJavaParser.ID, 0)

        def type_(self):
            return self.getTypedRuleContext(simplifiedJavaParser.TypeContext,0)


        def declarationParametersList(self):
            return self.getTypedRuleContext(simplifiedJavaParser.DeclarationParametersListContext,0)


        def getRuleIndex(self):
            return simplifiedJavaParser.RULE_functionDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionDeclaration" ):
                listener.enterFunctionDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionDeclaration" ):
                listener.exitFunctionDeclaration(self)




    def functionDeclaration(self):

        localctx = simplifiedJavaParser.FunctionDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_functionDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.match(simplifiedJavaParser.ID)
            self.state = 67
            self.match(simplifiedJavaParser.T__1)
            self.state = 69
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 16106127360) != 0):
                self.state = 68
                self.declarationParametersList()


            self.state = 71
            self.match(simplifiedJavaParser.T__2)
            self.state = 72
            self.match(simplifiedJavaParser.T__3)
            self.state = 75
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [30, 31, 32, 33]:
                self.state = 73
                self.type_()
                pass
            elif token in [5]:
                self.state = 74
                self.match(simplifiedJavaParser.T__4)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationParametersListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(simplifiedJavaParser.TypeContext)
            else:
                return self.getTypedRuleContext(simplifiedJavaParser.TypeContext,i)


        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(simplifiedJavaParser.ID)
            else:
                return self.getToken(simplifiedJavaParser.ID, i)

        def getRuleIndex(self):
            return simplifiedJavaParser.RULE_declarationParametersList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclarationParametersList" ):
                listener.enterDeclarationParametersList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclarationParametersList" ):
                listener.exitDeclarationParametersList(self)




    def declarationParametersList(self):

        localctx = simplifiedJavaParser.DeclarationParametersListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_declarationParametersList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.type_()
            self.state = 78
            self.match(simplifiedJavaParser.ID)
            self.state = 85
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 79
                self.match(simplifiedJavaParser.T__5)
                self.state = 80
                self.type_()
                self.state = 81
                self.match(simplifiedJavaParser.ID)
                self.state = 87
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MainFunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variableDeclarationArea(self):
            return self.getTypedRuleContext(simplifiedJavaParser.VariableDeclarationAreaContext,0)


        def cmdBlock(self):
            return self.getTypedRuleContext(simplifiedJavaParser.CmdBlockContext,0)


        def getRuleIndex(self):
            return simplifiedJavaParser.RULE_mainFunction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMainFunction" ):
                listener.enterMainFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMainFunction" ):
                listener.exitMainFunction(self)




    def mainFunction(self):

        localctx = simplifiedJavaParser.MainFunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_mainFunction)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self.match(simplifiedJavaParser.T__6)
            self.state = 89
            self.match(simplifiedJavaParser.T__3)
            self.state = 91
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==8:
                self.state = 90
                self.variableDeclarationArea()


            self.state = 94
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 274878347264) != 0):
                self.state = 93
                self.cmdBlock()


            self.state = 96
            self.match(simplifiedJavaParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableDeclarationAreaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variableDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(simplifiedJavaParser.VariableDeclarationContext)
            else:
                return self.getTypedRuleContext(simplifiedJavaParser.VariableDeclarationContext,i)


        def getRuleIndex(self):
            return simplifiedJavaParser.RULE_variableDeclarationArea

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableDeclarationArea" ):
                listener.enterVariableDeclarationArea(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableDeclarationArea" ):
                listener.exitVariableDeclarationArea(self)




    def variableDeclarationArea(self):

        localctx = simplifiedJavaParser.VariableDeclarationAreaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_variableDeclarationArea)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self.match(simplifiedJavaParser.T__7)
            self.state = 99
            self.match(simplifiedJavaParser.T__3)
            self.state = 101 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 100
                    self.variableDeclaration()

                else:
                    raise NoViableAltException(self)
                self.state = 103 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variableList(self):
            return self.getTypedRuleContext(simplifiedJavaParser.VariableListContext,0)


        def type_(self):
            return self.getTypedRuleContext(simplifiedJavaParser.TypeContext,0)


        def attributionList(self):
            return self.getTypedRuleContext(simplifiedJavaParser.AttributionListContext,0)


        def getRuleIndex(self):
            return simplifiedJavaParser.RULE_variableDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableDeclaration" ):
                listener.enterVariableDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableDeclaration" ):
                listener.exitVariableDeclaration(self)




    def variableDeclaration(self):

        localctx = simplifiedJavaParser.VariableDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_variableDeclaration)
        try:
            self.state = 114
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [38]:
                self.enterOuterAlt(localctx, 1)
                self.state = 105
                self.variableList()
                self.state = 106
                self.match(simplifiedJavaParser.T__3)
                self.state = 107
                self.type_()
                self.state = 108
                self.match(simplifiedJavaParser.T__8)
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 2)
                self.state = 110
                self.match(simplifiedJavaParser.T__9)
                self.state = 111
                self.attributionList()
                self.state = 112
                self.match(simplifiedJavaParser.T__8)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CmdBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def command(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(simplifiedJavaParser.CommandContext)
            else:
                return self.getTypedRuleContext(simplifiedJavaParser.CommandContext,i)


        def getRuleIndex(self):
            return simplifiedJavaParser.RULE_cmdBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCmdBlock" ):
                listener.enterCmdBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCmdBlock" ):
                listener.exitCmdBlock(self)




    def cmdBlock(self):

        localctx = simplifiedJavaParser.CmdBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_cmdBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 116
                self.command()
                self.state = 119 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 274878347264) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def controlCmd(self):
            return self.getTypedRuleContext(simplifiedJavaParser.ControlCmdContext,0)


        def attributionCmd(self):
            return self.getTypedRuleContext(simplifiedJavaParser.AttributionCmdContext,0)


        def ioCmd(self):
            return self.getTypedRuleContext(simplifiedJavaParser.IoCmdContext,0)


        def functionCall(self):
            return self.getTypedRuleContext(simplifiedJavaParser.FunctionCallContext,0)


        def expression(self):
            return self.getTypedRuleContext(simplifiedJavaParser.ExpressionContext,0)


        def getRuleIndex(self):
            return simplifiedJavaParser.RULE_command

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommand" ):
                listener.enterCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommand" ):
                listener.exitCommand(self)




    def command(self):

        localctx = simplifiedJavaParser.CommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_command)
        try:
            self.state = 137
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 121
                self.controlCmd()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 122
                self.attributionCmd()
                self.state = 123
                self.match(simplifiedJavaParser.T__8)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 125
                self.ioCmd()
                self.state = 126
                self.match(simplifiedJavaParser.T__8)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 128
                self.functionCall()
                self.state = 129
                self.match(simplifiedJavaParser.T__8)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 131
                self.match(simplifiedJavaParser.T__10)
                self.state = 132
                self.expression(0)
                self.state = 133
                self.match(simplifiedJavaParser.T__8)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 135
                self.match(simplifiedJavaParser.T__11)
                self.state = 136
                self.match(simplifiedJavaParser.T__8)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ControlCmdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ifCmd(self):
            return self.getTypedRuleContext(simplifiedJavaParser.IfCmdContext,0)


        def whileCmd(self):
            return self.getTypedRuleContext(simplifiedJavaParser.WhileCmdContext,0)


        def getRuleIndex(self):
            return simplifiedJavaParser.RULE_controlCmd

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterControlCmd" ):
                listener.enterControlCmd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitControlCmd" ):
                listener.exitControlCmd(self)




    def controlCmd(self):

        localctx = simplifiedJavaParser.ControlCmdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_controlCmd)
        try:
            self.state = 141
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13]:
                self.enterOuterAlt(localctx, 1)
                self.state = 139
                self.ifCmd()
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 2)
                self.state = 140
                self.whileCmd()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfCmdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(simplifiedJavaParser.ExpressionContext,0)


        def cmdBlock(self):
            return self.getTypedRuleContext(simplifiedJavaParser.CmdBlockContext,0)


        def elseCmd(self):
            return self.getTypedRuleContext(simplifiedJavaParser.ElseCmdContext,0)


        def getRuleIndex(self):
            return simplifiedJavaParser.RULE_ifCmd

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfCmd" ):
                listener.enterIfCmd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfCmd" ):
                listener.exitIfCmd(self)




    def ifCmd(self):

        localctx = simplifiedJavaParser.IfCmdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_ifCmd)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143
            self.match(simplifiedJavaParser.T__12)
            self.state = 144
            self.match(simplifiedJavaParser.T__1)
            self.state = 145
            self.expression(0)
            self.state = 146
            self.match(simplifiedJavaParser.T__2)
            self.state = 147
            self.match(simplifiedJavaParser.T__3)
            self.state = 149
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 274878347264) != 0):
                self.state = 148
                self.cmdBlock()


            self.state = 152
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==14:
                self.state = 151
                self.elseCmd()


            self.state = 154
            self.match(simplifiedJavaParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElseCmdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def cmdBlock(self):
            return self.getTypedRuleContext(simplifiedJavaParser.CmdBlockContext,0)


        def getRuleIndex(self):
            return simplifiedJavaParser.RULE_elseCmd

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElseCmd" ):
                listener.enterElseCmd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElseCmd" ):
                listener.exitElseCmd(self)




    def elseCmd(self):

        localctx = simplifiedJavaParser.ElseCmdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_elseCmd)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156
            self.match(simplifiedJavaParser.T__13)
            self.state = 157
            self.match(simplifiedJavaParser.T__3)
            self.state = 159
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 274878347264) != 0):
                self.state = 158
                self.cmdBlock()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileCmdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(simplifiedJavaParser.ExpressionContext,0)


        def cmdBlock(self):
            return self.getTypedRuleContext(simplifiedJavaParser.CmdBlockContext,0)


        def getRuleIndex(self):
            return simplifiedJavaParser.RULE_whileCmd

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileCmd" ):
                listener.enterWhileCmd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileCmd" ):
                listener.exitWhileCmd(self)




    def whileCmd(self):

        localctx = simplifiedJavaParser.WhileCmdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_whileCmd)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self.match(simplifiedJavaParser.T__14)
            self.state = 162
            self.match(simplifiedJavaParser.T__1)
            self.state = 163
            self.expression(0)
            self.state = 164
            self.match(simplifiedJavaParser.T__2)
            self.state = 165
            self.match(simplifiedJavaParser.T__3)
            self.state = 167
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 274878347264) != 0):
                self.state = 166
                self.cmdBlock()


            self.state = 169
            self.match(simplifiedJavaParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttributionListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attributionCmd(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(simplifiedJavaParser.AttributionCmdContext)
            else:
                return self.getTypedRuleContext(simplifiedJavaParser.AttributionCmdContext,i)


        def getRuleIndex(self):
            return simplifiedJavaParser.RULE_attributionList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttributionList" ):
                listener.enterAttributionList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttributionList" ):
                listener.exitAttributionList(self)




    def attributionList(self):

        localctx = simplifiedJavaParser.AttributionListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_attributionList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            self.attributionCmd()
            self.state = 176
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 172
                self.match(simplifiedJavaParser.T__5)
                self.state = 173
                self.attributionCmd()
                self.state = 178
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttributionCmdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(simplifiedJavaParser.ID, 0)

        def expression(self):
            return self.getTypedRuleContext(simplifiedJavaParser.ExpressionContext,0)


        def getRuleIndex(self):
            return simplifiedJavaParser.RULE_attributionCmd

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttributionCmd" ):
                listener.enterAttributionCmd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttributionCmd" ):
                listener.exitAttributionCmd(self)




    def attributionCmd(self):

        localctx = simplifiedJavaParser.AttributionCmdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_attributionCmd)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 179
            self.match(simplifiedJavaParser.ID)
            self.state = 180
            self.match(simplifiedJavaParser.T__15)
            self.state = 181
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IoCmdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressionList(self):
            return self.getTypedRuleContext(simplifiedJavaParser.ExpressionListContext,0)


        def variableList(self):
            return self.getTypedRuleContext(simplifiedJavaParser.VariableListContext,0)


        def getRuleIndex(self):
            return simplifiedJavaParser.RULE_ioCmd

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIoCmd" ):
                listener.enterIoCmd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIoCmd" ):
                listener.exitIoCmd(self)




    def ioCmd(self):

        localctx = simplifiedJavaParser.IoCmdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_ioCmd)
        try:
            self.state = 193
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [17]:
                self.enterOuterAlt(localctx, 1)
                self.state = 183
                self.match(simplifiedJavaParser.T__16)
                self.state = 184
                self.match(simplifiedJavaParser.T__1)
                self.state = 185
                self.expressionList()
                self.state = 186
                self.match(simplifiedJavaParser.T__2)
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 2)
                self.state = 188
                self.match(simplifiedJavaParser.T__17)
                self.state = 189
                self.match(simplifiedJavaParser.T__1)
                self.state = 190
                self.variableList()
                self.state = 191
                self.match(simplifiedJavaParser.T__2)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(simplifiedJavaParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(simplifiedJavaParser.ExpressionContext,i)


        def getRuleIndex(self):
            return simplifiedJavaParser.RULE_expressionList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionList" ):
                listener.enterExpressionList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionList" ):
                listener.exitExpressionList(self)




    def expressionList(self):

        localctx = simplifiedJavaParser.ExpressionListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_expressionList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 195
            self.expression(0)
            self.state = 200
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 196
                self.match(simplifiedJavaParser.T__5)
                self.state = 197
                self.expression(0)
                self.state = 202
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.e1 = None # ExpressionContext
            self.op = None # Token
            self.e2 = None # ExpressionContext

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(simplifiedJavaParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(simplifiedJavaParser.ExpressionContext,i)


        def functionCall(self):
            return self.getTypedRuleContext(simplifiedJavaParser.FunctionCallContext,0)


        def literal(self):
            return self.getTypedRuleContext(simplifiedJavaParser.LiteralContext,0)


        def ID(self):
            return self.getToken(simplifiedJavaParser.ID, 0)

        def getRuleIndex(self):
            return simplifiedJavaParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = simplifiedJavaParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 36
        self.enterRecursionRule(localctx, 36, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 215
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.state = 204
                self.match(simplifiedJavaParser.T__1)
                self.state = 205
                self.expression(0)
                self.state = 206
                self.match(simplifiedJavaParser.T__2)
                pass

            elif la_ == 2:
                self.state = 208
                self.match(simplifiedJavaParser.T__18)
                self.state = 209
                self.expression(9)
                pass

            elif la_ == 3:
                self.state = 210
                self.match(simplifiedJavaParser.T__19)
                self.state = 211
                self.expression(8)
                pass

            elif la_ == 4:
                self.state = 212
                self.functionCall()
                pass

            elif la_ == 5:
                self.state = 213
                self.literal()
                pass

            elif la_ == 6:
                self.state = 214
                self.match(simplifiedJavaParser.ID)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 231
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 229
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
                    if la_ == 1:
                        localctx = simplifiedJavaParser.ExpressionContext(self, _parentctx, _parentState)
                        localctx.e1 = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 217
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 218
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==21 or _la==22):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 219
                        localctx.e2 = self.expression(8)
                        pass

                    elif la_ == 2:
                        localctx = simplifiedJavaParser.ExpressionContext(self, _parentctx, _parentState)
                        localctx.e1 = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 220
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 221
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==20 or _la==23):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 222
                        localctx.e2 = self.expression(7)
                        pass

                    elif la_ == 3:
                        localctx = simplifiedJavaParser.ExpressionContext(self, _parentctx, _parentState)
                        localctx.e1 = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 223
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 224
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 251658240) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 225
                        localctx.e2 = self.expression(6)
                        pass

                    elif la_ == 4:
                        localctx = simplifiedJavaParser.ExpressionContext(self, _parentctx, _parentState)
                        localctx.e1 = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 226
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 227
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==28 or _la==29):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 228
                        localctx.e2 = self.expression(5)
                        pass

             
                self.state = 233
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class FunctionCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(simplifiedJavaParser.ID, 0)

        def expressionList(self):
            return self.getTypedRuleContext(simplifiedJavaParser.ExpressionListContext,0)


        def getRuleIndex(self):
            return simplifiedJavaParser.RULE_functionCall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionCall" ):
                listener.enterFunctionCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionCall" ):
                listener.exitFunctionCall(self)




    def functionCall(self):

        localctx = simplifiedJavaParser.FunctionCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_functionCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 234
            self.match(simplifiedJavaParser.ID)
            self.state = 235
            self.match(simplifiedJavaParser.T__1)
            self.state = 237
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 532577517572) != 0):
                self.state = 236
                self.expressionList()


            self.state = 239
            self.match(simplifiedJavaParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(simplifiedJavaParser.ID, 0)

        def variableList(self):
            return self.getTypedRuleContext(simplifiedJavaParser.VariableListContext,0)


        def getRuleIndex(self):
            return simplifiedJavaParser.RULE_variableList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableList" ):
                listener.enterVariableList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableList" ):
                listener.exitVariableList(self)




    def variableList(self):

        localctx = simplifiedJavaParser.VariableListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_variableList)
        try:
            self.state = 245
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 241
                self.match(simplifiedJavaParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 242
                self.match(simplifiedJavaParser.ID)
                self.state = 243
                self.match(simplifiedJavaParser.T__5)
                self.state = 244
                self.variableList()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return simplifiedJavaParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)




    def type_(self):

        localctx = simplifiedJavaParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 247
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 16106127360) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(simplifiedJavaParser.INT, 0)

        def FLOAT(self):
            return self.getToken(simplifiedJavaParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(simplifiedJavaParser.STRING, 0)

        def BOOL(self):
            return self.getToken(simplifiedJavaParser.BOOL, 0)

        def getRuleIndex(self):
            return simplifiedJavaParser.RULE_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)




    def literal(self):

        localctx = simplifiedJavaParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 249
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 257698037760) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[18] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 4)
         




