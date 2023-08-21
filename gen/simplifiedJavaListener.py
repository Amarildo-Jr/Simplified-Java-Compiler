# Generated from C:/Repositórios/Projetos/UFPI/Compiladores/Simplified-Java-Compiler\simplifiedJava.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .simplifiedJavaParser import simplifiedJavaParser
else:
    from simplifiedJavaParser import simplifiedJavaParser

# This class defines a complete listener for a parse tree produced by simplifiedJavaParser.
class simplifiedJavaListener(ParseTreeListener):

    # Enter a parse tree produced by simplifiedJavaParser#program.
    def enterProgram(self, ctx:simplifiedJavaParser.ProgramContext):
        pass

    # Exit a parse tree produced by simplifiedJavaParser#program.
    def exitProgram(self, ctx:simplifiedJavaParser.ProgramContext):
        pass


    # Enter a parse tree produced by simplifiedJavaParser#functionsBlock.
    def enterFunctionsBlock(self, ctx:simplifiedJavaParser.FunctionsBlockContext):
        pass

    # Exit a parse tree produced by simplifiedJavaParser#functionsBlock.
    def exitFunctionsBlock(self, ctx:simplifiedJavaParser.FunctionsBlockContext):
        pass


    # Enter a parse tree produced by simplifiedJavaParser#function.
    def enterFunction(self, ctx:simplifiedJavaParser.FunctionContext):
        pass

    # Exit a parse tree produced by simplifiedJavaParser#function.
    def exitFunction(self, ctx:simplifiedJavaParser.FunctionContext):
        pass


    # Enter a parse tree produced by simplifiedJavaParser#functionDeclaration.
    def enterFunctionDeclaration(self, ctx:simplifiedJavaParser.FunctionDeclarationContext):
        pass

    # Exit a parse tree produced by simplifiedJavaParser#functionDeclaration.
    def exitFunctionDeclaration(self, ctx:simplifiedJavaParser.FunctionDeclarationContext):
        pass


    # Enter a parse tree produced by simplifiedJavaParser#declarationParametersList.
    def enterDeclarationParametersList(self, ctx:simplifiedJavaParser.DeclarationParametersListContext):
        pass

    # Exit a parse tree produced by simplifiedJavaParser#declarationParametersList.
    def exitDeclarationParametersList(self, ctx:simplifiedJavaParser.DeclarationParametersListContext):
        pass


    # Enter a parse tree produced by simplifiedJavaParser#mainFunction.
    def enterMainFunction(self, ctx:simplifiedJavaParser.MainFunctionContext):
        pass

    # Exit a parse tree produced by simplifiedJavaParser#mainFunction.
    def exitMainFunction(self, ctx:simplifiedJavaParser.MainFunctionContext):
        pass


    # Enter a parse tree produced by simplifiedJavaParser#variableDeclarationArea.
    def enterVariableDeclarationArea(self, ctx:simplifiedJavaParser.VariableDeclarationAreaContext):
        pass

    # Exit a parse tree produced by simplifiedJavaParser#variableDeclarationArea.
    def exitVariableDeclarationArea(self, ctx:simplifiedJavaParser.VariableDeclarationAreaContext):
        pass


    # Enter a parse tree produced by simplifiedJavaParser#variableDeclaration.
    def enterVariableDeclaration(self, ctx:simplifiedJavaParser.VariableDeclarationContext):
        pass

    # Exit a parse tree produced by simplifiedJavaParser#variableDeclaration.
    def exitVariableDeclaration(self, ctx:simplifiedJavaParser.VariableDeclarationContext):
        pass


    # Enter a parse tree produced by simplifiedJavaParser#cmdBlock.
    def enterCmdBlock(self, ctx:simplifiedJavaParser.CmdBlockContext):
        pass

    # Exit a parse tree produced by simplifiedJavaParser#cmdBlock.
    def exitCmdBlock(self, ctx:simplifiedJavaParser.CmdBlockContext):
        pass


    # Enter a parse tree produced by simplifiedJavaParser#command.
    def enterCommand(self, ctx:simplifiedJavaParser.CommandContext):
        pass

    # Exit a parse tree produced by simplifiedJavaParser#command.
    def exitCommand(self, ctx:simplifiedJavaParser.CommandContext):
        pass


    # Enter a parse tree produced by simplifiedJavaParser#controlCmd.
    def enterControlCmd(self, ctx:simplifiedJavaParser.ControlCmdContext):
        pass

    # Exit a parse tree produced by simplifiedJavaParser#controlCmd.
    def exitControlCmd(self, ctx:simplifiedJavaParser.ControlCmdContext):
        pass


    # Enter a parse tree produced by simplifiedJavaParser#ifCmd.
    def enterIfCmd(self, ctx:simplifiedJavaParser.IfCmdContext):
        pass

    # Exit a parse tree produced by simplifiedJavaParser#ifCmd.
    def exitIfCmd(self, ctx:simplifiedJavaParser.IfCmdContext):
        pass


    # Enter a parse tree produced by simplifiedJavaParser#elseCmd.
    def enterElseCmd(self, ctx:simplifiedJavaParser.ElseCmdContext):
        pass

    # Exit a parse tree produced by simplifiedJavaParser#elseCmd.
    def exitElseCmd(self, ctx:simplifiedJavaParser.ElseCmdContext):
        pass


    # Enter a parse tree produced by simplifiedJavaParser#whileCmd.
    def enterWhileCmd(self, ctx:simplifiedJavaParser.WhileCmdContext):
        pass

    # Exit a parse tree produced by simplifiedJavaParser#whileCmd.
    def exitWhileCmd(self, ctx:simplifiedJavaParser.WhileCmdContext):
        pass


    # Enter a parse tree produced by simplifiedJavaParser#attributionList.
    def enterAttributionList(self, ctx:simplifiedJavaParser.AttributionListContext):
        pass

    # Exit a parse tree produced by simplifiedJavaParser#attributionList.
    def exitAttributionList(self, ctx:simplifiedJavaParser.AttributionListContext):
        pass


    # Enter a parse tree produced by simplifiedJavaParser#attributionCmd.
    def enterAttributionCmd(self, ctx:simplifiedJavaParser.AttributionCmdContext):
        pass

    # Exit a parse tree produced by simplifiedJavaParser#attributionCmd.
    def exitAttributionCmd(self, ctx:simplifiedJavaParser.AttributionCmdContext):
        pass


    # Enter a parse tree produced by simplifiedJavaParser#ioCmd.
    def enterIoCmd(self, ctx:simplifiedJavaParser.IoCmdContext):
        pass

    # Exit a parse tree produced by simplifiedJavaParser#ioCmd.
    def exitIoCmd(self, ctx:simplifiedJavaParser.IoCmdContext):
        pass


    # Enter a parse tree produced by simplifiedJavaParser#expressionList.
    def enterExpressionList(self, ctx:simplifiedJavaParser.ExpressionListContext):
        pass

    # Exit a parse tree produced by simplifiedJavaParser#expressionList.
    def exitExpressionList(self, ctx:simplifiedJavaParser.ExpressionListContext):
        pass


    # Enter a parse tree produced by simplifiedJavaParser#expression.
    def enterExpression(self, ctx:simplifiedJavaParser.ExpressionContext):
        pass

    # Exit a parse tree produced by simplifiedJavaParser#expression.
    def exitExpression(self, ctx:simplifiedJavaParser.ExpressionContext):
        pass


    # Enter a parse tree produced by simplifiedJavaParser#functionCall.
    def enterFunctionCall(self, ctx:simplifiedJavaParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by simplifiedJavaParser#functionCall.
    def exitFunctionCall(self, ctx:simplifiedJavaParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by simplifiedJavaParser#variableList.
    def enterVariableList(self, ctx:simplifiedJavaParser.VariableListContext):
        pass

    # Exit a parse tree produced by simplifiedJavaParser#variableList.
    def exitVariableList(self, ctx:simplifiedJavaParser.VariableListContext):
        pass


    # Enter a parse tree produced by simplifiedJavaParser#type.
    def enterType(self, ctx:simplifiedJavaParser.TypeContext):
        pass

    # Exit a parse tree produced by simplifiedJavaParser#type.
    def exitType(self, ctx:simplifiedJavaParser.TypeContext):
        pass


    # Enter a parse tree produced by simplifiedJavaParser#literal.
    def enterLiteral(self, ctx:simplifiedJavaParser.LiteralContext):
        pass

    # Exit a parse tree produced by simplifiedJavaParser#literal.
    def exitLiteral(self, ctx:simplifiedJavaParser.LiteralContext):
        pass



del simplifiedJavaParser