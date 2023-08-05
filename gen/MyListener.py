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
                    exit(f"Variable {var} is constant")
                else:
                    if ctx.exprType == "int" and self.symbolTable[var]["type"] == "float":
                        ctx.exprType = "float"
                    elif ctx.exprType == "float" and self.symbolTable[var]["type"] == "int":
                        ctx.exprType = "int"
                    elif ctx.exprType != self.symbolTable[var]["type"]:
                        exit(f"Variable {var} is not of type {ctx.exprType}")
            else:
                exit(f"Variable {var} not declared")
        else:
            if var in self.symbolTable:
                exit(f"Variable {var} already declared")
            else:
                self.symbolTable[var] = {"isConst": True, "type": ctx.exprType}

    # Exit a parse tree produced by simplifiedJavaParser#ioCmd.
    def exitIoCmd(self, ctx: simplifiedJavaParser.IoCmdContext):
        pass

    # Exit a parse tree produced by simplifiedJavaParser#expressionList.
    def exitExpressionList(self, ctx: simplifiedJavaParser.ExpressionListContext):
        pass

    # OK
    def exitExpression(self, ctx: simplifiedJavaParser.ExpressionContext):
        ctx.exprType = None
        if ctx.getChildCount() == 1:
            if ctx.ID():
                varIdentifier = ctx.ID().getText()
                if varIdentifier in self.symbolTable:
                    ctx.exprType = self.symbolTable[varIdentifier]["type"]
                else:
                    exit(f"Variable {varIdentifier} not declared")
            elif ctx.literal():
                ctx.exprType = ctx.literal().varType
            elif ctx.functionCall():
                pass  # TODO: Check if function exists
        elif ctx.getChildCount() == 2:
            op = ctx.getChild(0).getText()
            expression = ctx.expression(0)
            if op == '!':
                if expression.exprType == "bool":
                    ctx.exprType = "bool"
                else:
                    exit(f"{expression.getText()} is not of type bool")
            elif op == '-':
                if expression.exprType == "int" or expression.exprType == "float":
                    ctx.exprType = expression.exprType
                else:
                    exit(f"{expression.getText()} is not of type int or float")
        elif ctx.getChildCount() == 3:
            if ctx.getChild(0) == '(':
                ctx.exprType = ctx.expression(1).exprType
            else:
                op = ctx.getChild(1).getText()
                expr1 = ctx.expression(0)
                expr2 = ctx.expression(1)
                if op == '+' or op == '-' or op == '*':
                    if expr1.exprType != "int" and expr1.exprType != "float":
                        exit(f"{expr1.getText()} is not of type int or float")
                    elif expr2.exprType != "int" and expr2.exprType != "float":
                        exit(f"{expr2.getText()} is not of type int or float")
                    elif expr1.exprType == expr2.exprType:
                        ctx.exprType = expr1.exprType
                    elif expr1.exprType == "float" or expr2.exprType == "float":
                        ctx.exprType = "float"
                elif op == '/':
                    if expr1.exprType != "int" and expr1.exprType != "float":
                        exit(f"{expr1.getText()} is not of type int or float")
                    elif expr2.exprType != "int" and expr2.exprType != "float":
                        exit(f"{expr2.getText()} is not of type int or float")
                    else:
                        ctx.exprType = "float"
                elif op == '<' or op == '>' or op == '<=' or op == '>=' or op == '==' or op == '!=':
                    if expr1.exprType == expr2.exprType:
                        ctx.exprType = "bool"
                    elif expr1.exprType == "int" and expr2.exprType == "float":
                        ctx.exprType = "bool"
                    elif expr1.exprType == "float" and expr2.exprType == "int":
                        ctx.exprType = "bool"
                    else:
                        exit(f"Cannot compare {expr1.exprType} with {expr2.exprType}")

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
