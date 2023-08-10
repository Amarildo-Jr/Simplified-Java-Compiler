from .simplifiedJavaListener import simplifiedJavaListener

if __name__ is not None and "." in __name__:
    from .simplifiedJavaParser import simplifiedJavaParser
else:
    from simplifiedJavaParser import simplifiedJavaParser


class MyListener(simplifiedJavaListener):
    symbolTable: dict = {}

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
        functionName = ctx.getChild(0).ID().getText()
        if self.symbolTable[functionName]["hasReturn"] and self.symbolTable[functionName].get("value") is None:
            exit(f"Function {functionName} expects {self.symbolTable[functionName]['type']} return")

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
            self.symbolTable[functionName] = {"hasReturn": hasReturn, "type": functionReturn, "parameters": {}}

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

        for var, varType in parametersDict.items():
            if var in self.symbolTable:
                exit(f"Variable {var} already declared")
            else:
                self.symbolTable[functionName]["parameters"].setdefault(var, {"isInit": True, "isConst": False, "type": varType})

    # Exit a parse tree produced by simplifiedJavaParser#functionCall.
    def exitFunctionCall(self, ctx: simplifiedJavaParser.FunctionCallContext):
        functionName = ctx.ID().getText()
        functionParameters = self.symbolTable[functionName].get("parameters")

        parametersQuantity = 0
        if functionParameters is not None:
            parametersQuantity = len(functionParameters)

        parametersReceivedQuantity = 0
        if ctx.expressionList() is not None:
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
        line = ctx.start.line
        column = ctx.start.column
        ancestor = ctx.parentCtx
        while type(ancestor) != simplifiedJavaParser.MainFunctionContext and type(ancestor) != simplifiedJavaParser.FunctionContext:
            ancestor = ancestor.parentCtx
        if ctx.getChildCount() == 4:
            ctx.varType = ctx.type_().varType
            ctx.variableList = ctx.variableList().variableList
            for var in ctx.variableList:
                if type(ancestor) == simplifiedJavaParser.MainFunctionContext:
                    symbolTable = self.symbolTable
                    if var in symbolTable:
                        exit(f"line {line}:{column} Variable {var} already declared")
                    else:
                        self.symbolTable[var] = {"isInit": False, "isConst": False, "type": ctx.varType}
                elif type(ancestor) == simplifiedJavaParser.FunctionContext:
                    functionName = ancestor.getChild(0).ID().getText()
                    parameters = self.symbolTable[functionName]["parameters"]
                    symbolTable = dict(self.symbolTable[functionName], **parameters)
                    if var in symbolTable:
                        exit(f"line {line}:{column} Variable {var} already declared")
                    else:
                        self.symbolTable[functionName][var] = {"isInit": False, "isConst": False, "type": ctx.varType}

    # Exit a parse tree produced by simplifiedJavaParser#cmdBlock.
    def exitCmdBlock(self, ctx: simplifiedJavaParser.CmdBlockContext):
        pass

    # Exit a parse tree produced by simplifiedJavaParser#command.
    def exitCommand(self, ctx: simplifiedJavaParser.CommandContext):
        line = ctx.start.line
        column = ctx.start.column
        ancestor = ctx.parentCtx
        while type(ancestor) != simplifiedJavaParser.MainFunctionContext and type(ancestor) != simplifiedJavaParser.FunctionContext:
            ancestor = ancestor.parentCtx
        child = ctx.getChild(0)
        if child.getText() == "return":
            functionCtx = ctx.parentCtx.parentCtx
            functionDeclarationCtx = functionCtx.getChild(0)

            if functionDeclarationCtx.type_() is None:
                exit(f"line {line}:{column} Function {functionDeclarationCtx.ID().getText()} does not expect return")

            if type(functionCtx) == simplifiedJavaParser.FunctionContext:
                if functionDeclarationCtx.type_().getText() != ctx.expression().exprType:
                    exit(f"line {line}:{column} Function {functionDeclarationCtx.ID().getText()} expects {functionDeclarationCtx.type_().getText()} type return, but {ctx.expression().exprType} was given")
            else:
                exit(f"line {line}:{column} Return command only allowed in functions")

            functionName = functionDeclarationCtx.ID().getText()
            self.symbolTable[functionName]["value"] = ctx.expression().value
        if child.getText() == "break":
            while type(ctx.parentCtx) != simplifiedJavaParser.WhileCmdContext and type(ctx.parentCtx) != simplifiedJavaParser.ProgramContext:
                ctx = ctx.parentCtx
            if type(ctx.parentCtx) == simplifiedJavaParser.ProgramContext:
                exit(f"line {line}:{column} Break command only allowed in while commands")
        if type(child) == simplifiedJavaParser.IoCmdContext:
            ioCmdCtx = ctx.getChild(0)
            if ioCmdCtx.getChild(0).getText() == "print":
                pass
            if ioCmdCtx.getChild(0).getText() == "scanf":
                variableList = ioCmdCtx.variableList().variableList
                if type(ancestor) == simplifiedJavaParser.MainFunctionContext:
                    for var in variableList:
                        symbolTable = self.symbolTable
                        if type(ancestor) == simplifiedJavaParser.MainFunctionContext:
                            symbolTable = self.symbolTable
                        elif type(ancestor) == simplifiedJavaParser.FunctionContext:
                            functionName = ancestor.getChild(0).ID().getText()
                            symbolTable = self.symbolTable[functionName]
                        if var not in symbolTable:
                            exit(f"line {line}:{column} Variable {var} not declared")
                        elif symbolTable[var]["isConst"]:
                            exit(f"line {line}:{column} Variable {var} is constant")
                        else:
                            symbolTable[var]["isInit"] = True
                else:
                    functionName = ancestor.getChild(0).ID().getText()
                    for var in variableList:
                        if var not in self.symbolTable[functionName]:
                            exit(f"line {line}:{column} Variable {var} not declared")
                        elif self.symbolTable[functionName][var]["isConst"]:
                            exit(f"line {line}:{column} Variable {var} is constant")
                        else:
                            self.symbolTable[functionName][var]["isInit"] = True

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
        line = ctx.start.line
        column = ctx.start.column
        parent = ctx.parentCtx
        ancestor = ctx.parentCtx
        while type(ancestor) != simplifiedJavaParser.MainFunctionContext and type(ancestor) != simplifiedJavaParser.FunctionContext:
            ancestor = ancestor.parentCtx
        var = ctx.ID().getText()
        ctx.exprType = ctx.expression().exprType
        symbolTable = self.symbolTable
        if type(ancestor) == simplifiedJavaParser.MainFunctionContext:
            symbolTable = self.symbolTable
        elif type(ancestor) == simplifiedJavaParser.FunctionContext:
            functionName = ancestor.getChild(0).ID().getText()
            parameters = self.symbolTable[functionName]["parameters"]
            symbolTable = dict(self.symbolTable[functionName], **parameters)
        if type(parent) == simplifiedJavaParser.CommandContext:
            if var in symbolTable:
                if symbolTable[var]["isConst"]:
                    exit(f"line {line}:{column} Variable {var} is constant")
                else:
                    symbolTable[var]["isInit"] = True
                    if ctx.exprType == "int" and symbolTable[var]["type"] == "float":
                        ctx.exprType = "float"
                    elif ctx.exprType == "float" and symbolTable[var]["type"] == "int":
                        ctx.exprType = "int"
                    elif ctx.exprType != symbolTable[var]["type"]:
                        exit(f"line {line}:{column} Variable {var} is not of type {ctx.exprType}")

                symbolTable[var]["value"] = ctx.expression().value
            else:
                exit(f"line {line}:{column} Variable {var} not declared")
        else:
            if var in symbolTable:
                exit(f"line {line}:{column} Variable {var} already declared")
            else:
                symbolTable[var] = {"isInit": True, "isConst": True, "type": ctx.exprType, "value": ctx.expression().value}



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

    # OK
    def exitExpression(self, ctx: simplifiedJavaParser.ExpressionContext):
        line = ctx.start.line
        column = ctx.start.column
        ancestor = ctx.parentCtx
        while type(ancestor) != simplifiedJavaParser.MainFunctionContext and type(ancestor) != simplifiedJavaParser.FunctionContext:
            ancestor = ancestor.parentCtx
        ctx.exprType = None
        ctx.value = None
        if ctx.getChildCount() == 1:
            if ctx.ID():
                var = ctx.ID().getText()
                symbolTable = self.symbolTable
                if type(ancestor) == simplifiedJavaParser.MainFunctionContext:
                    symbolTable = self.symbolTable
                elif type(ancestor) == simplifiedJavaParser.FunctionContext:
                    functionName = ancestor.getChild(0).ID().getText()
                    parameters = self.symbolTable[functionName]["parameters"]
                    symbolTable = dict(self.symbolTable[functionName], **parameters)
                if var in symbolTable:
                    if not symbolTable[var]["isInit"]:
                        exit(f"line {line}:{column} Variable {var} not initialized")
                    else:
                        ctx.exprType = symbolTable[var]["type"]
                else:
                    exit(f"line {line}:{column} Variable {var} not declared")
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
        elif ctx.getChildCount() == 2:
            op = ctx.getChild(0).getText()
            expression = ctx.expression(0)
            if op == '!':
                if expression.exprType == "bool":
                    ctx.exprType = "bool"
                else:
                    exit(f"line {line}:{column} {expression.getText()} is not of type bool")
            elif op == '-':
                if expression.exprType == "int" or expression.exprType == "float":
                    ctx.exprType = expression.exprType
                else:
                    exit(f"line {line}:{column} {expression.getText()} is not of type int or float")
        elif ctx.getChildCount() == 3:
            if ctx.getChild(0).getText() == '(':
                ctx.exprType = ctx.expression(0).exprType
            else:
                op = ctx.getChild(1).getText()
                expr1 = ctx.expression(0)
                expr2 = ctx.expression(1)
                if op == '+' or op == '-' or op == '*':
                    if expr1.exprType != "int" and expr1.exprType != "float":
                        exit(f"line {line}:{column} {expr1.getText()} is not of type int or float")
                    elif expr2.exprType != "int" and expr2.exprType != "float":
                        exit(f"line {line}:{column} {expr2.getText()} is not of type int or float")
                    elif expr1.exprType == expr2.exprType:
                        ctx.exprType = expr1.exprType
                    elif expr1.exprType == "float" or expr2.exprType == "float":
                        ctx.exprType = "float"
                elif op == '/':
                    if expr1.exprType != "int" and expr1.exprType != "float":
                        exit(f"line {line}:{column} {expr1.getText()} is not of type int or float")
                    elif expr2.exprType != "int" and expr2.exprType != "float":
                        exit(f"line {line}:{column} {expr2.getText()} is not of type int or float")
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
                        exit(f"line {line}:{column} Cannot compare {expr1.exprType} with {expr2.exprType}")

                # if op == '+':
                #     ctx.value = expr1.value + expr2.value
                #     print(ctx.value)

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
