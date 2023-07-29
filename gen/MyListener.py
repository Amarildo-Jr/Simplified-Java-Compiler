from antlr4 import *

from .simplifiedJavaListener import simplifiedJavaListener

if __name__ is not None and "." in __name__:
    from .simplifiedJavaParser import simplifiedJavaParser
else:
    from simplifiedJavaParser import simplifiedJavaParser


class MyListener(simplifiedJavaListener):
    symbolTable = {}

    # Enter a parse tree produced by simplifiedJavaParser#program.
    def enterProgram(self, ctx: simplifiedJavaParser.ProgramContext):
        pass

    # Exit a parse tree produced by simplifiedJavaParser#program.
    def exitProgram(self, ctx: simplifiedJavaParser.ProgramContext):
        pass

    # Exit a parse tree produced by simplifiedJavaParser#functionsBlock.
    def exitFunctionsBlock(self, ctx: simplifiedJavaParser.FunctionsBlockContext):
        pass

    # Exit a parse tree produced by simplifiedJavaParser#function.
    def exitFunction(self, ctx: simplifiedJavaParser.FunctionContext):
        pass

    # Exit a parse tree produced by simplifiedJavaParser#functionDeclaration.
    def exitFunctionDeclaration(self, ctx: simplifiedJavaParser.FunctionDeclarationContext):
        pass

    # Exit a parse tree produced by simplifiedJavaParser#functionCall.
    def exitFunctionCall(self, ctx: simplifiedJavaParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by simplifiedJavaParser#declarationParametersList.
    def exitDeclarationParametersList(self, ctx: simplifiedJavaParser.DeclarationParametersListContext):
        pass

    # Exit a parse tree produced by simplifiedJavaParser#mainFunction.
    def exitMainFunction(self, ctx: simplifiedJavaParser.MainFunctionContext):
        pass

    # OK
    def exitVariableDeclarationArea(self, ctx: simplifiedJavaParser.VariableDeclarationAreaContext):
        print(self.symbolTable)

    # OK
    def exitVariableDeclaration(self, ctx: simplifiedJavaParser.VariableDeclarationContext):
        if ctx.getChildCount() == 4:
            ctx.varType = ctx.type_().varType
            ctx.variableList = ctx.variableList().variableList
            for var in ctx.variableList:
                if var in self.symbolTable:
                    exit("Variable " + var + " already declared")
                else:
                    self.symbolTable[var] = {"isConst": False, "type": ctx.varType}

    # Exit a parse tree produced by simplifiedJavaParser#cmdBlock.
    def exitCmdBlock(self, ctx: simplifiedJavaParser.CmdBlockContext):
        pass

    # Exit a parse tree produced by simplifiedJavaParser#command.
    def exitCommand(self, ctx: simplifiedJavaParser.CommandContext):
        pass

    # Exit a parse tree produced by simplifiedJavaParser#controlCmd.
    def exitControlCmd(self, ctx: simplifiedJavaParser.ControlCmdContext):
        pass

    # Exit a parse tree produced by simplifiedJavaParser#ifCmd.
    def exitIfCmd(self, ctx: simplifiedJavaParser.IfCmdContext):
        pass

    # Exit a parse tree produced by simplifiedJavaParser#elseCmd.
    def exitElseCmd(self, ctx: simplifiedJavaParser.ElseCmdContext):
        pass

    # Exit a parse tree produced by simplifiedJavaParser#whileCmd.
    def exitWhileCmd(self, ctx: simplifiedJavaParser.WhileCmdContext):
        pass

    # OK
    def exitAttributionCmd(self, ctx: simplifiedJavaParser.AttributionCmdContext):
        parent = ctx.parentCtx
        var = ctx.ID().getText()
        ctx.exprType = ctx.expression().exprType
        if type(parent) == simplifiedJavaParser.CommandContext:
            if var in self.symbolTable:
                if self.symbolTable[var]["isConst"]:
                    exit("Variable " + var + " is const")
                else:
                    if ctx.exprType != self.symbolTable[var]["type"]:
                        exit("Variable " + var + " is not of type " + ctx.exprType)
            else:
                exit("Variable " + var + " not declared")
        else:
            if var in self.symbolTable:
                exit("Variable " + var + " already declared")
            else:
                self.symbolTable[var] = {"isConst": True, "type": ctx.exprType}

    # Exit a parse tree produced by simplifiedJavaParser#ioCmd.
    def exitIoCmd(self, ctx: simplifiedJavaParser.IoCmdContext):
        pass

    # Exit a parse tree produced by simplifiedJavaParser#expressionList.
    def exitExpressionList(self, ctx: simplifiedJavaParser.ExpressionListContext):
        pass

    # TODO
    def exitExpression(self, ctx: simplifiedJavaParser.ExpressionContext):
        ctx.exprType = None
        if ctx.getChildCount() == 1:
            if ctx.ID():
                identifier = ctx.ID().getText()
                if identifier in self.symbolTable:
                    ctx.exprType = self.symbolTable[identifier]["type"]
                else:
                    exit("Variable " + ctx.ID().getText() + " not declared")
            elif ctx.literal():
                ctx.exprType = ctx.literal().varType
            elif ctx.functionCall():
                pass  # TODO: Check if function exists

    # OK
    def exitVariableList(self, ctx: simplifiedJavaParser.VariableListContext):
        ctx.variableList = ctx.getText().split(',')

    # OK
    def exitType(self, ctx: simplifiedJavaParser.TypeContext):
        ctx.varType = ctx.getText()

    # OK
    def exitLiteral(self, ctx: simplifiedJavaParser.LiteralContext):
        ctx.varType = None
        ctx.value = ctx.getText()
        if ctx.INT():
            ctx.varType = "int"
        elif ctx.FLOAT():
            ctx.varType = "float"
        elif ctx.STRING():
            ctx.varType = "str"
        elif ctx.BOOL():
            ctx.varType = "bool"
