from antlr4 import *

from .simplifiedJavaListener import simplifiedJavaListener

if __name__ is not None and "." in __name__:
    from .simplifiedJavaParser import simplifiedJavaParser
else:
    from simplifiedJavaParser import simplifiedJavaParser


class MyListener(simplifiedJavaListener):
    symbolTable = {}
    functionDefault = {}

    # Enter a parse tree produced by simplifiedJavaParser#program.
    def enterProgram(self, ctx: simplifiedJavaParser.ProgramContext):
        pass

    # Exit a parse tree produced by simplifiedJavaParser#program.
    def exitProgram(self, ctx: simplifiedJavaParser.ProgramContext):
        pass

    # Enter a parse tree produced by simplifiedJavaParser#functionsBlock.
    def enterFunctionsBlock(self, ctx: simplifiedJavaParser.FunctionsBlockContext):
        pass

    # Exit a parse tree produced by simplifiedJavaParser#functionsBlock.
    def exitFunctionsBlock(self, ctx: simplifiedJavaParser.FunctionsBlockContext):
        pass

    # Exit a parse tree produced by simplifiedJavaParser#function.
    def exitFunction(self, ctx: simplifiedJavaParser.FunctionContext):
        pass

    def enterFunctionDeclaration(self, ctx: simplifiedJavaParser.FunctionDeclarationContext):
        functionName = ctx.ID().getText()
        try:
            functionReturn = ctx.type_().getText()
        except AttributeError:
            functionReturn = "void"

        if functionName in self.symbolTable:
            exit(f"Function {functionName} already declared")
        else:
            hasReturn = True if functionReturn != "void" else False
            self.symbolTable[functionName] = {"hasReturn": hasReturn, "type": functionReturn}

    # Exit a parse tree produced by simplifiedJavaParser#functionDeclaration.
    def exitFunctionDeclaration(self, ctx: simplifiedJavaParser.FunctionDeclarationContext):
        pass

    # Exit a parse tree produced by simplifiedJavaParser#declarationParametersList.
    def exitDeclarationParametersList(self, ctx: simplifiedJavaParser.DeclarationParametersListContext):
        typesList = ctx.type_()
        varList = ctx.ID()
        functionName = ctx.parentCtx.ID().getText()

        parametersDict = {}
        for i in range(len(varList)):
            parametersDict[f'{varList[i].getText()}'] = typesList[i].getText()
        ctx.parametersDict = parametersDict

        self.symbolTable[functionName].setdefault("parameters", {})
        for var, varType in parametersDict.items():
            if var in self.symbolTable:
                exit(f"Variable {var} already declared")
            else:
                self.symbolTable[functionName]["parameters"].setdefault(var, {"isConst": False, "type": varType})

    # Exit a parse tree produced by simplifiedJavaParser#functionCall.
    def exitFunctionCall(self, ctx: simplifiedJavaParser.FunctionCallContext):
        functionName = ctx.ID().getText()
        parametersQuantity = len(self.symbolTable[functionName]["parameters"])
        parametersReceivedQuantity = ctx.expressionList().expressionQuantity

        if functionName not in self.symbolTable:
            exit(f"Function {functionName} not declared")
        if parametersQuantity != parametersReceivedQuantity:
            exit(f"Function {functionName} expects {parametersQuantity} parameters, but {parametersReceivedQuantity} were given")

        count = 0
        for key, value in self.symbolTable[functionName]["parameters"].items():
            varName = ctx.expressionList().expressionParameters[count]
            if value["type"] != self.symbolTable[varName]["type"]:
                exit(f"Function {functionName} expects {value['type']} type for parameter {key}, but {self.symbolTable[varName]['type']} was given")
            count += 1

        ctx.functionName = functionName
        ctx.functionReturn = self.symbolTable[functionName]["type"]
        ctx.hasReturn = self.symbolTable[functionName]["hasReturn"]

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
                    exit(f"Variable {var} already declared")
                else:
                    self.symbolTable[var] = {"isConst": False, "type": ctx.varType, "value": None}

    # Exit a parse tree produced by simplifiedJavaParser#cmdBlock.
    def exitCmdBlock(self, ctx: simplifiedJavaParser.CmdBlockContext):
        pass

    # Exit a parse tree produced by simplifiedJavaParser#command.
    def exitCommand(self, ctx: simplifiedJavaParser.CommandContext):
        if ctx.getChild(0).getText() == "return":
            functionCtx = ctx.parentCtx.parentCtx
            functionDeclarationCtx = functionCtx.getChild(0)

            if functionDeclarationCtx.type_() is None:
                exit(f"Function {functionDeclarationCtx.ID().getText()} does not expect return")

            if type(functionCtx) == simplifiedJavaParser.FunctionContext:
                if functionDeclarationCtx.type_().getText() != ctx.expression().exprType:
                    exit(f"Function {functionDeclarationCtx.ID().getText()} expects {functionDeclarationCtx.type_().getText()} type, but {ctx.expression().exprType} was given")
            else:
                exit("Return command only allowed in functions")

            functionName = functionDeclarationCtx.ID().getText()
            self.symbolTable[functionName]["value"] = self.symbolTable[ctx.expression().ID().getText()]["value"]

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
                    exit(f"Variable {var} is const")
                if ctx.exprType != self.symbolTable[var]["type"]:
                    exit(f"Variable {var} is not of type {ctx.exprType}")

                self.symbolTable[var]["value"] = ctx.expression().value
            else:
                exit(f"Variable {var} not declared")
        else:
            if var in self.symbolTable:
                exit(f"Variable {var} already declared")
            else:
                self.symbolTable[var] = {"isConst": True, "type": ctx.exprType, "value": ctx.expression().value}

    # Exit a parse tree produced by simplifiedJavaParser#ioCmd.
    def exitIoCmd(self, ctx: simplifiedJavaParser.IoCmdContext):
        pass

    # Exit a parse tree produced by simplifiedJavaParser#expressionList.
    def exitExpressionList(self, ctx: simplifiedJavaParser.ExpressionListContext):
        expressionQuantity = len(ctx.expression())
        ctx.expressionQuantity = expressionQuantity

        expressionParameters = []
        for expression in ctx.expression():
            expressionParameters.append(expression.getText())

        ctx.expressionParameters = expressionParameters

    # TODO
    def exitExpression(self, ctx: simplifiedJavaParser.ExpressionContext):
        ctx.exprType = None
        ctx.value = None
        if ctx.getChildCount() == 1:
            if ctx.ID():
                identifier = ctx.ID().getText()
                if identifier in self.symbolTable:
                    ctx.exprType = self.symbolTable[identifier]["type"]
                else:
                    exit(f"Variable {ctx.ID().getText()} not declared")
            elif ctx.literal():
                ctx.exprType = ctx.literal().varType
                ctx.value = ctx.literal().value
            elif ctx.functionCall():
                functionName = ctx.functionCall().ID().getText()
                if functionName not in self.symbolTable:
                    exit(f"Function {functionName} not declared")

                if self.symbolTable[functionName]["hasReturn"]:
                    ctx.exprType = self.symbolTable[functionName]["type"]
                    ctx.value = self.symbolTable[functionName]["value"]

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
