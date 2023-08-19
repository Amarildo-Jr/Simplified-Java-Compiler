from .simplifiedJavaListener import simplifiedJavaListener

if __name__ is not None and "." in __name__:
    from .simplifiedJavaParser import simplifiedJavaParser
else:
    from simplifiedJavaParser import simplifiedJavaParser


class MyListener(simplifiedJavaListener):
    symbolTable: dict = {}

    def __init__(self):
        super().__init__()
        self.jasminFile = open("teste.j", "w")
        self.jasminFile.write(".class public teste\n")
        self.jasminFile.write(".super java/lang/Object\n")
        self.qtVariables = 1
        self.qtLabels = 0
        self.hasScanf = False

    @staticmethod
    def translateTypeJasmin(type_, cmd=False):
        if type_ == "int":
            return "I"
        elif type_ == "float":
            return "F"
        elif type_ == "bool":
            if cmd:
                return "I"
            return "Z"
        elif type_ == "str":
            if cmd:
                return "A"
            else:
                return "Ljava/lang/String;"
        elif type_ == "void":
            if cmd:
                return ""
            return "V"

    @staticmethod
    def translateOperatorJasmin(operator):
        if operator == "+":
            return "add"
        elif operator == "-":
            return "sub"
        elif operator == "*":
            return "mul"
        elif operator == "/":
            return "div"
        elif operator == "<":
            return "lt"
        elif operator == ">":
            return "gt"
        elif operator == "<=":
            return "le"
        elif operator == ">=":
            return "ge"
        elif operator == "==":
            return "eq"
        elif operator == "!=":
            return "ne"

    def readerInit(self, firstAvailableAddress=0):
        return (f"new java/io/BufferedReader\n"
                f"dup\n"
                f"new java/io/InputStreamReader\n"
                f"dup\n"
                f"getstatic java/lang/System/in Ljava/io/InputStream;\n"
                f"invokespecial java/io/InputStreamReader/<init>(Ljava/io/InputStream;)V\n"
                f"invokespecial java/io/BufferedReader/<init>(Ljava/io/Reader;)V\n"
                f"astore {firstAvailableAddress}\n")

    def createBooleanStructure(self, isInAttribution, isFloat=False, isString=False):
        if isString:
            code = f"_op_ Ltrue{self.qtLabels}\n"
            if isInAttribution:
                code += f"iconst_0\n"
            code += f"placeholder\n"
            code += f"goto Lafter{self.qtLabels}\n"
            code += f"Ltrue{self.qtLabels}:\n"
            if isInAttribution:
                code += f"iconst_1\n"
            code += f"placeholder\n"
            code += f"Lafter{self.qtLabels}:\n"
            self.qtLabels += 1
        elif isFloat:
            code = f"fcmpl\n"
            code += f"_op_ Ltrue{self.qtLabels}\n"
            if isInAttribution:
                code += f"iconst_0\n"
            code += f"placeholder\n"
            code += f"goto Lafter{self.qtLabels}\n"
            code += f"Ltrue{self.qtLabels}:\n"
            if isInAttribution:
                code += f"iconst_1\n"
            code += f"placeholder\n"
            code += f"Lafter{self.qtLabels}:\n"
            self.qtLabels += 1
        else:
            code = f" Ltrue{self.qtLabels}\n"
            if isInAttribution:
                code += f"iconst_0\n"
            code += f"placeholder\n"
            code += f"goto Lafter{self.qtLabels}\n"
            code += f"Ltrue{self.qtLabels}:\n"
            if isInAttribution:
                code += f"iconst_1\n"
            code += f"placeholder\n"
            code += f"Lafter{self.qtLabels}:\n"
            self.qtLabels += 1
        return code

    # Enter a parse tree produced by simplifiedJavaParser#program.
    def enterProgram(self, ctx: simplifiedJavaParser.ProgramContext):
        pass

    # Exit a parse tree produced by simplifiedJavaParser#program.
    def exitProgram(self, ctx: simplifiedJavaParser.ProgramContext):
        ctx.code = ""
        if ctx.functionsBlock() is not None:
            ctx.code = ctx.functionsBlock().code
        ctx.code += ctx.mainFunction().code
        self.jasminFile.write(ctx.code)

    # Exit a parse tree produced by simplifiedJavaParser#functionsBlock.
    def exitFunctionsBlock(self, ctx: simplifiedJavaParser.FunctionsBlockContext):
        ctx.code = ""
        for function in ctx.function():
            ctx.code += function.code

    # Exit a parse tree produced by simplifiedJavaParser#function.
    def exitFunction(self, ctx: simplifiedJavaParser.FunctionContext):
        functionName = ctx.functionDeclaration().ID().getText()
        functionReturn = ctx.functionDeclaration().type_()
        if functionReturn is not None:
            functionReturn = functionReturn.getText()
        else:
            functionReturn = "void"
        qtParameters = len(self.symbolTable[functionName]["parameters"])
        qtLocalVariables = len(self.symbolTable[functionName]) - 3
        ctx.code = f".method public static {functionName}("
        for key, value in self.symbolTable[functionName]["parameters"].items():
            ctx.code += self.translateTypeJasmin(value["type"])
        ctx.code += f"){self.translateTypeJasmin(functionReturn)}\n"
        ctx.code += f".limit locals {qtLocalVariables + qtParameters}\n"
        ctx.code += f".limit stack 100\n"
        if ctx.variableDeclarationArea() is not None:
            ctx.code += ctx.variableDeclarationArea().code
        if ctx.cmdBlock() is not None:
            ctx.code += ctx.cmdBlock().code
        ctx.code += f"{self.translateTypeJasmin(functionReturn, True).lower()}return\n"
        ctx.code += f".end method\n"

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
            self.symbolTable[functionName] = {"qtVariables": 0, "hasReturn": hasReturn, "hasScanf": False,
                                              "type": functionReturn, "parameters": {}}

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
            if varList[i].getText() in parametersDict:
                exit(f"Parameter {varList[i].getText()} already declared")
            parametersDict[f'{varList[i].getText()}'] = typesList[i].getText()
        ctx.parametersDict = parametersDict

        for var, varType in parametersDict.items():
            if var in self.symbolTable:
                exit(f"Variable {var} already declared")
            else:
                self.symbolTable[functionName]["parameters"].setdefault(var, {"isInit": True, "isConst": False,
                                                                              "type": varType, "jasminAddress":
                                                                                  self.symbolTable[functionName][
                                                                                      "qtVariables"]})
                self.symbolTable[functionName]["qtVariables"] += 1

    def exitFunctionCall(self, ctx: simplifiedJavaParser.FunctionCallContext):
        ctx.code = ""
        line = ctx.start.line
        column = ctx.start.column
        functionName = ctx.ID().getText()
        if functionName not in self.symbolTable:
            exit(f"line {line}:{column} Function {functionName} not declared")
        functionParameters = self.symbolTable[functionName].get("parameters")

        parametersQuantity = 0
        if functionParameters is not None:
            parametersQuantity = len(functionParameters)

        parametersReceivedQuantity = 0
        if ctx.expressionList() is not None:
            parametersReceivedQuantity = ctx.expressionList().expressionQuantity

        if functionName not in self.symbolTable:
            exit(f"line {line}:{column} Function {functionName} not declared")
        if parametersQuantity != parametersReceivedQuantity:
            exit(f"line {line}:{column} Function {functionName} expects {parametersQuantity} parameters, "
                 f"but {parametersReceivedQuantity} were given")

        count = 0
        for key, value in self.symbolTable[functionName]["parameters"].items():
            expression = ctx.expressionList().expressionParameters[count]
            ctx.code += expression.code
            if expression.exprType == "int" and value["type"] == "float":
                ctx.code += f"i2f\n"
                count += 1
                continue
            elif expression.exprType == "float" and value["type"] == "int":
                ctx.code += f"f2i\n"
                count += 1
                continue
            if expression.exprType != value["type"]:
                exit(f"line {line}:{column} Function {functionName} expects {value['type']} type for parameter {key}, "
                     f"but {expression.exprType} was given")
            count += 1

        ctx.functionName = functionName
        ctx.functionReturn = self.symbolTable[functionName]["type"]
        ctx.hasReturn = self.symbolTable[functionName]["hasReturn"]
        ctx.code += f"invokestatic teste/{functionName}("
        for key, value in self.symbolTable[functionName]["parameters"].items():
            ctx.code += self.translateTypeJasmin(value["type"])
        ctx.code += f"){self.translateTypeJasmin(self.symbolTable[functionName]['type'])}\n"

    # Exit a parse tree produced by simplifiedJavaParser#mainFunction.
    def exitMainFunction(self, ctx: simplifiedJavaParser.MainFunctionContext):
        qtVariables = len(self.symbolTable)
        ctx.code = f".method public static main([Ljava/lang/String;)V\n"
        ctx.code += f".limit locals {qtVariables}\n"
        ctx.code += f".limit stack 100\n"
        if self.hasScanf:
            ctx.code += self.readerInit(0)
        if ctx.cmdBlock() is not None:
            ctx.code += f"{ctx.cmdBlock().code}"
        ctx.code += f"return\n"
        ctx.code += f".end method\n"

    # OK
    def exitVariableDeclarationArea(self, ctx: simplifiedJavaParser.VariableDeclarationAreaContext):
        ctx.code = ""
        for variableDeclaration in ctx.variableDeclaration():
            ctx.code += variableDeclaration.code
        print(self.symbolTable)

    # OK
    def exitVariableDeclaration(self, ctx: simplifiedJavaParser.VariableDeclarationContext):
        ctx.code = ""
        line = ctx.start.line
        column = ctx.start.column
        ancestor = ctx.parentCtx
        while type(ancestor) != simplifiedJavaParser.MainFunctionContext and type(
                ancestor) != simplifiedJavaParser.FunctionContext:
            ancestor = ancestor.parentCtx
        if ctx.attributionList() is not None:
            ctx.code += ctx.attributionList().code
        if ctx.getChildCount() == 4:
            ctx.varType = ctx.type_().varType
            variableList = ctx.variableList().variableList
            for var in variableList:
                if type(ancestor) == simplifiedJavaParser.MainFunctionContext:
                    symbolTable = self.symbolTable
                    if var in symbolTable:
                        exit(f"line {line}:{column} Variable {var} already declared")
                    else:
                        self.symbolTable[var] = {"isInit": False, "isConst": False, "type": ctx.varType,
                                                 "jasminAddress": self.qtVariables}
                        self.qtVariables += 1
                elif type(ancestor) == simplifiedJavaParser.FunctionContext:
                    functionName = ancestor.getChild(0).ID().getText()
                    parameters = self.symbolTable[functionName]["parameters"]
                    functions = dict([(functionName, self.symbolTable[functionName]) for functionName
                                      in self.symbolTable.keys() if "hasReturn" in self.symbolTable[functionName]])
                    symbolTable = dict(self.symbolTable[functionName], **parameters)
                    symbolTable = dict(symbolTable, **functions)
                    if var in symbolTable:
                        exit(f"line {line}:{column} Variable {var} already declared")
                    else:
                        self.symbolTable[functionName][var] = {"isInit": False, "isConst": False, "type": ctx.varType,
                                                               "jasminAddress": self.symbolTable[functionName][
                                                                   "qtVariables"]}
                        self.symbolTable[functionName]["qtVariables"] += 1

    # Exit a parse tree produced by simplifiedJavaParser#cmdBlock.
    def exitCmdBlock(self, ctx: simplifiedJavaParser.CmdBlockContext):
        ctx.code = ""
        for cmd in ctx.command():
            ctx.code += cmd.code

    # Exit a parse tree produced by simplifiedJavaParser#command.
    def exitCommand(self, ctx: simplifiedJavaParser.CommandContext):
        ctx.code = ""
        line = ctx.start.line
        column = ctx.start.column
        ancestor = ctx.parentCtx
        while (type(ancestor) != simplifiedJavaParser.MainFunctionContext and type(ancestor)
               != simplifiedJavaParser.FunctionContext):
            ancestor = ancestor.parentCtx
        child = ctx.getChild(0)
        if ctx.controlCmd() is not None:
            ctx.code = ctx.controlCmd().code
        if ctx.attributionCmd() is not None:
            ctx.code = ctx.attributionCmd().code
        if ctx.ioCmd() is not None:
            ctx.code = ctx.ioCmd().code
        if ctx.functionCall() is not None:
            ctx.code = ctx.functionCall().code
            if ctx.functionCall().hasReturn:
                ctx.code += f"pop\n"
        if child.getText() == "return":
            if type(ancestor) == simplifiedJavaParser.MainFunctionContext:
                exit(f"line {line}:{column} Return command only allowed in functions")
            else:
                functionCtx = ancestor
                functionDeclarationCtx = functionCtx.getChild(0)

                if functionDeclarationCtx.type_() is None:
                    exit(
                        f"line {line}:{column} Function {functionDeclarationCtx.ID().getText()} does not expect return")

                if type(functionCtx) == simplifiedJavaParser.FunctionContext:
                    functionType = functionDeclarationCtx.type_().getText()
                    if functionType != ctx.expression().exprType:
                        exit(
                            f"line {line}:{column} Function {functionDeclarationCtx.ID().getText()} "
                            f"expects {functionType} type return, "
                            f"but {ctx.expression().exprType} was given")
                    ctx.code = ctx.expression().code
                    ctx.code += f"{self.translateTypeJasmin(functionType, True).lower()}return\n"
                functionName = functionDeclarationCtx.ID().getText()
                self.symbolTable[functionName]["value"] = ctx.expression().value
        if child.getText() == "break":
            while type(ctx.parentCtx) != simplifiedJavaParser.WhileCmdContext and type(
                    ctx.parentCtx) != simplifiedJavaParser.ProgramContext:
                ctx = ctx.parentCtx
            if type(ctx.parentCtx) == simplifiedJavaParser.ProgramContext:
                exit(f"line {line}:{column} Break command only allowed in while commands")

    # Exit a parse tree produced by simplifiedJavaParser#controlCmd.
    def exitControlCmd(self, ctx: simplifiedJavaParser.ControlCmdContext):
        ctx.code = ""
        if ctx.whileCmd() is not None:
            ctx.code = ctx.whileCmd().code
        if ctx.ifCmd() is not None:
            ctx.code = ctx.ifCmd().code

    # Exit a parse tree produced by simplifiedJavaParser#ifCmd.
    def exitIfCmd(self, ctx: simplifiedJavaParser.IfCmdContext):
        ctx.code = ""
        ctx.code += ctx.expression().code
        if ctx.elseCmd() is not None:
            ctx.code = ctx.code.replace("placeholder", ctx.elseCmd().code, 1)
        else:
            ctx.code = ctx.code.replace("placeholder", "", 1)
        if ctx.cmdBlock() is not None:
            ctx.code = ctx.code.replace("placeholder", f"{ctx.cmdBlock().code}", 1)
        else:
            ctx.code = ctx.code.replace("placeholder", "", 1)

    # Exit a parse tree produced by simplifiedJavaParser#elseCmd.
    def exitElseCmd(self, ctx: simplifiedJavaParser.ElseCmdContext):
        if ctx.cmdBlock() is not None:
            ctx.code = ctx.cmdBlock().code
        else:
            ctx.code = ""

    # Exit a parse tree produced by simplifiedJavaParser#whileCmd.
    def exitWhileCmd(self, ctx: simplifiedJavaParser.WhileCmdContext):
        ctx.code = ""
        ctx.code += f"Lbegin{self.qtLabels}:\n"
        ctx.code += ctx.expression().code
        ctx.code = ctx.code.replace("placeholder", "", 1)
        if ctx.cmdBlock() is not None:
            ctx.code = ctx.code.replace("placeholder", f"{ctx.cmdBlock().code}\ngoto Lbegin{self.qtLabels}", 1)
        else:
            ctx.code = ctx.code.replace("placeholder", f"goto Lbegin{self.qtLabels}", 1)
        self.qtLabels += 1

    def exitAttributionList(self, ctx: simplifiedJavaParser.AttributionListContext):
        ctx.code = ""
        for attributionCmd in ctx.attributionCmd():
            ctx.code += attributionCmd.code

    # OK
    def exitAttributionCmd(self, ctx: simplifiedJavaParser.AttributionCmdContext):
        ctx.code = ctx.expression().code
        line = ctx.start.line
        column = ctx.start.column
        parent = ctx.parentCtx
        ancestor = ctx.parentCtx
        while type(ancestor) != simplifiedJavaParser.MainFunctionContext and type(
                ancestor) != simplifiedJavaParser.FunctionContext:
            ancestor = ancestor.parentCtx
        var = ctx.ID().getText()
        ctx.exprType = ctx.expression().exprType
        symbolTable = self.symbolTable
        if type(ancestor) == simplifiedJavaParser.MainFunctionContext:
            symbolTable = self.symbolTable
        elif type(ancestor) == simplifiedJavaParser.FunctionContext:
            functionName = ancestor.getChild(0).ID().getText()
            parameters = self.symbolTable[functionName]["parameters"]
            functions = dict([(functionName, self.symbolTable[functionName]) for functionName in self.symbolTable.keys()
                              if "hasReturn" in self.symbolTable[functionName]])
            symbolTable = dict(self.symbolTable[functionName], **parameters)
            symbolTable = dict(symbolTable, **functions)
        if type(parent) == simplifiedJavaParser.CommandContext:
            if var in symbolTable:
                if symbolTable[var]["isConst"]:
                    exit(f"line {line}:{column} Variable {var} is constant")
                else:
                    symbolTable[var]["isInit"] = True
                    varType = symbolTable[var]["type"]
                    if ctx.exprType == "int" and varType == "float":
                        ctx.exprType = "float"
                        ctx.code += f"i2f\n"
                    elif ctx.exprType == "float" and varType == "int":
                        ctx.exprType = "int"
                        ctx.code += f"f2i\n"
                    elif ctx.exprType != varType:
                        exit(f"line {line}:{column} Variable {var} is not of type {ctx.exprType}")
                    if ctx.exprType != "bool":
                        ctx.code += (f"{self.translateTypeJasmin(varType, True).lower()}store"
                                     f" {symbolTable[var]['jasminAddress']}\n")
                    else:
                        ctx.code = ctx.code.replace(f"placeholder",
                                                    f"{self.translateTypeJasmin(varType, True).lower()}store"
                                                    f" {symbolTable[var]['jasminAddress']}")

                symbolTable[var]["value"] = ctx.expression().value
            else:
                exit(f"line {line}:{column} Variable {var} not declared")
        else:
            if var in symbolTable:
                exit(f"line {line}:{column} Variable {var} already declared")
            else:
                if type(ancestor) == simplifiedJavaParser.MainFunctionContext:
                    symbolTable[var] = {"isInit": True, "isConst": True, "type": ctx.exprType,
                                        "value": ctx.expression().value, "jasminAddress": self.qtVariables}
                    self.qtVariables += 1
                    ctx.code += f"{self.translateTypeJasmin(ctx.exprType, True).lower()}store {symbolTable[var]['jasminAddress']}\n"
                elif type(ancestor) == simplifiedJavaParser.FunctionContext:
                    symbolTable[var] = {"isInit": True, "isConst": True, "type": ctx.exprType,
                                        "value": ctx.expression().value, "jasminAddress": symbolTable["qtVariables"]}
                    symbolTable["qtVariables"] += 1
                    ctx.code += f"{self.translateTypeJasmin(ctx.exprType, True).lower()}store {symbolTable[var]['jasminAddress']}\n"

    # Exit a parse tree produced by simplifiedJavaParser#ioCmd.
    def exitIoCmd(self, ctx: simplifiedJavaParser.IoCmdContext):
        ctx.code = ""
        line = ctx.start.line
        column = ctx.start.column
        ancestor = ctx.parentCtx
        while (type(ancestor) != simplifiedJavaParser.MainFunctionContext and type(ancestor)
               != simplifiedJavaParser.FunctionContext):
            ancestor = ancestor.parentCtx
        child = ctx.getChild(0)
        if child.getText() == "scanf":
            variableList = ctx.variableList().variableList
            for var in variableList:
                symbolTable = self.symbolTable
                if type(ancestor) == simplifiedJavaParser.MainFunctionContext:
                    symbolTable = self.symbolTable
                elif type(ancestor) == simplifiedJavaParser.FunctionContext:
                    functionName = ancestor.getChild(0).ID().getText()
                    parameters = self.symbolTable[functionName]["parameters"]
                    symbolTable = dict(self.symbolTable[functionName], **parameters)
                if var not in symbolTable:
                    exit(f"line {line}:{column} Variable {var} not declared")
                elif symbolTable[var]["isConst"]:
                    exit(f"line {line}:{column} Variable {var} is constant")
                else:
                    symbolTable[var]["isInit"] = True
                    if type(ancestor) == simplifiedJavaParser.MainFunctionContext:
                        if not self.hasScanf:
                            self.hasScanf = True
                    if type(ancestor) == simplifiedJavaParser.FunctionContext:
                        symbolTable["hasScanf"] = True
                    if symbolTable[var]["type"] == "int":
                        ctx.code += f"aload 0\n"
                        ctx.code += f"invokevirtual java/io/BufferedReader/readLine()Ljava/lang/String;\n"
                        ctx.code += f"invokestatic java/lang/Integer/parseInt(Ljava/lang/String;)I\n"
                        ctx.code += f"istore {symbolTable[var]['jasminAddress']}\n"
                    elif symbolTable[var]["type"] == "float":
                        ctx.code += f"aload 0\n"
                        ctx.code += f"invokevirtual java/io/BufferedReader/readLine()Ljava/lang/String;\n"
                        ctx.code += f"invokestatic java/lang/Float/parseFloat(Ljava/lang/String;)F\n"
                        ctx.code += f"fstore {symbolTable[var]['jasminAddress']}\n"
                    elif symbolTable[var]["type"] == "bool":
                        ctx.code += f"aload 0\n"
                        ctx.code += f"invokevirtual java/io/BufferedReader/readLine()Ljava/lang/String;\n"
                        ctx.code += f"invokestatic java/lang/Boolean/parseBoolean(Ljava/lang/String;)Z\n"
                        ctx.code += f"istore {symbolTable[var]['jasminAddress']}\n"
                    else:
                        ctx.code += f"aload 0\n"
                        ctx.code += f"invokevirtual java/io/BufferedReader/readLine()Ljava/lang/String;\n"
                        ctx.code += f"astore {symbolTable[var]['jasminAddress']}\n"
        if child.getText() == "print":
            for expression in ctx.expressionList().expressionParameters:
                if expression.exprType is None:
                    exit(f"line {line}:{column} Expression not valid")
                elif expression.exprType == "bool":
                    ctx.code += expression.code
                    ctx.code = ctx.code.replace("placeholder",
                                                f"getstatic java/lang/System/out Ljava/io/PrintStream;\n"
                                                f"iconst_0\n"
                                                f"invokevirtual java/io/PrintStream/println("
                                                f"{self.translateTypeJasmin(expression.exprType)})V\n", 1)
                    ctx.code = ctx.code.replace("placeholder",
                                                f"getstatic java/lang/System/out Ljava/io/PrintStream;\n"
                                                f"iconst_1\n"
                                                f"invokevirtual java/io/PrintStream/println("
                                                f"{self.translateTypeJasmin(expression.exprType)})V\n", 1)
                else:
                    ctx.code += f"getstatic java/lang/System/out Ljava/io/PrintStream;\n"
                    ctx.code += expression.code
                    ctx.code += f"invokevirtual java/io/PrintStream/println({self.translateTypeJasmin(expression.exprType)})V\n"


    # Exit a parse tree produced by simplifiedJavaParser#expressionList.
    def exitExpressionList(self, ctx: simplifiedJavaParser.ExpressionListContext):
        ctx.code = ""
        expressionQuantity = len(ctx.expression())
        ctx.expressionQuantity = expressionQuantity

        expressionParameters = []
        for expression in ctx.expression():
            ctx.code += expression.code
            expressionParameters.append(expression)

        ctx.expressionParameters = expressionParameters

    # OK
    def exitExpression(self, ctx: simplifiedJavaParser.ExpressionContext):
        ctx.code = ""
        line = ctx.start.line
        column = ctx.start.column
        ancestor = ctx.parentCtx
        while type(ancestor) != simplifiedJavaParser.MainFunctionContext and type(
                ancestor) != simplifiedJavaParser.FunctionContext:
            ancestor = ancestor.parentCtx

        isInAttribution = False
        temp = ctx.parentCtx
        while temp is not None:
            if type(temp) == simplifiedJavaParser.AttributionCmdContext:
                isInAttribution = True
                break
            temp = temp.parentCtx

        ctx.exprType = None
        ctx.value = None
        ctx.code = ""
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
                        ctx.code = f"{self.translateTypeJasmin(ctx.exprType, True).lower()}load {symbolTable[var]['jasminAddress']}\n"
                        if ctx.exprType == "bool":
                            ctx.code += f"ifne"
                            ctx.code += self.createBooleanStructure(isInAttribution)
                else:
                    exit(f"line {line}:{column} Variable {var} not declared")
            elif ctx.literal():
                ctx.exprType = ctx.literal().varType
                ctx.value = ctx.literal().value
                if ctx.exprType == "bool":
                    if ctx.value == "true":
                        ctx.value = 1
                    elif ctx.value == "false":
                        ctx.value = 0
                    ctx.code = f"ldc {ctx.value}\n"
                    ctx.code += f"ifne"
                    ctx.code += self.createBooleanStructure(isInAttribution)
                else:
                    ctx.code = f"ldc {ctx.value}\n"
            elif ctx.functionCall():
                functionName = ctx.functionCall().ID().getText()
                if functionName not in self.symbolTable:
                    exit(f"line {line}:{column} Function {functionName} not declared")
                if self.symbolTable[functionName]["hasReturn"]:
                    ctx.exprType = self.symbolTable[functionName]["type"]
                ctx.code = ctx.functionCall().code
                if ctx.exprType == "bool":
                    ctx.code += f"ifne"
                    ctx.code += self.createBooleanStructure(isInAttribution)
        elif ctx.getChildCount() == 2:
            op = ctx.getChild(0).getText()
            expression = ctx.expression(0)
            if op == '!':
                if expression.exprType == "bool":
                    ctx.exprType = "bool"
                    ctx.code = expression.code
                    ctx.code += f"iconst_1\n"
                    ctx.code += f"ixor\n"
                else:
                    exit(f"line {line}:{column} {expression.getText()} is not of type bool")
            elif op == '-':
                if expression.exprType == "int" or expression.exprType == "float":
                    ctx.exprType = expression.exprType
                    ctx.code = expression.code
                    if op == "int":
                        ctx.code += f"ineg\n"
                    elif op == "float":
                        ctx.code += f"fneg\n"
                else:
                    exit(f"line {line}:{column} {expression.getText()} is not of type int or float")
        elif ctx.getChildCount() == 3:
            if ctx.getChild(0).getText() == '(':
                ctx.exprType = ctx.expression(0).exprType
                ctx.code = ctx.expression(0).code
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
                        ctx.code = expr1.code
                        ctx.code += expr2.code
                        ctx.code += (f"{self.translateTypeJasmin(expr1.exprType, True).lower()}"
                                     f"{self.translateOperatorJasmin(op)}\n")
                    elif expr1.exprType == "float" or expr2.exprType == "float":
                        ctx.exprType = "float"
                        if expr1.exprType == "int":
                            ctx.code = expr1.code
                            ctx.code += f"i2f\n"
                            ctx.code += expr2.code
                            ctx.code += (f"{self.translateTypeJasmin(expr2.exprType, True).lower()}"
                                         f"{self.translateOperatorJasmin(op)}\n")
                        elif expr2.exprType == "int":
                            ctx.code = expr1.code
                            ctx.code += expr2.code
                            ctx.code += f"i2f\n"
                            ctx.code += (f"{self.translateTypeJasmin(expr1.exprType, True).lower()}"
                                         f"{self.translateOperatorJasmin(op)}\n")
                    else:
                        exit(
                            f"line {line}:{column} Cannot operate {expr1.exprType} with {expr2.exprType} "
                            f"{expr1.getText()} {op} {expr2.getText()}")
                elif op == '/':
                    if expr1.exprType != "int" and expr1.exprType != "float":
                        exit(f"line {line}:{column} {expr1.getText()} is not of type int or float")
                    elif expr2.exprType != "int" and expr2.exprType != "float":
                        exit(f"line {line}:{column} {expr2.getText()} is not of type int or float")
                    elif expr1.exprType == expr2.exprType:
                        ctx.exprType = expr1.exprType
                        ctx.code = expr1.code
                        ctx.code += expr2.code
                        ctx.code += (f"{self.translateTypeJasmin(expr1.exprType, True).lower()}"
                                     f"{self.translateOperatorJasmin(op)}\n")
                    else:
                        ctx.exprType = "float"
                        if expr1.exprType == "int":
                            ctx.code = expr1.code
                            ctx.code += f"i2f\n"
                            ctx.code += expr2.code
                            ctx.code += (f"{self.translateTypeJasmin(expr2.exprType, True).lower()}"
                                         f"{self.translateOperatorJasmin(op)}\n")
                        elif expr2.exprType == "int":
                            ctx.code = expr1.code
                            ctx.code += expr2.code
                            ctx.code += f"i2f\n"
                            ctx.code += (f"{self.translateTypeJasmin(expr1.exprType, True).lower()}"
                                         f"{self.translateOperatorJasmin(op)}\n")
                elif op == '<' or op == '>' or op == '<=' or op == '>=':
                    if expr1.exprType == expr2.exprType and expr1.exprType != "bool":
                        ctx.exprType = "bool"
                        ctx.code = expr1.code
                        ctx.code += expr2.code
                    elif expr1.exprType == "int" and expr2.exprType == "float":
                        ctx.exprType = "bool"
                        ctx.code = expr1.code
                        ctx.code += f"i2f\n"
                        ctx.code += expr2.code
                    elif expr1.exprType == "float" and expr2.exprType == "int":
                        ctx.exprType = "bool"
                        ctx.code = expr1.code
                        ctx.code += expr2.code
                        ctx.code += f"i2f\n"
                    else:
                        exit(
                            f"line {line}:{column} Cannot compare {expr1.exprType} "
                            f"with {expr2.exprType} {expr1.getText()} {op} {expr2.getText()}")

                    if expr1.exprType == "float" or expr2.exprType == "float":
                        ctx.code += self.createBooleanStructure(isInAttribution, isFloat=True)
                        ctx.code = ctx.code.replace("_op_", f"if{self.translateOperatorJasmin(op)}", 1)
                    elif expr1.exprType == "str":
                        ctx.code += f"invokevirtual java/lang/String/compareTo(Ljava/lang/String;)I\n"
                        ctx.code += self.createBooleanStructure(isInAttribution, isString=True)
                        ctx.code = ctx.code.replace("_op_", f"if{self.translateOperatorJasmin(op)}", 1)
                    else:
                        ctx.code += (f"if_{self.translateTypeJasmin(expr1.exprType, True).lower()}"
                                     f"cmp{self.translateOperatorJasmin(op)}")
                        ctx.code += self.createBooleanStructure(isInAttribution)
                elif op == '==' or op == '!=':
                    if expr1.exprType == expr2.exprType:
                        if expr1.exprType == "bool":
                            exit(f"line {line}:{column} Cannot concatenate boolean expressions "
                                 f"{expr1.getText()} {op} {expr2.getText()}")
                        else:
                            ctx.exprType = "bool"
                            ctx.code = expr1.code
                            ctx.code += expr2.code
                    elif expr1.exprType == "int" and expr2.exprType == "float":
                        expr1.exprType = "float"
                        ctx.exprType = "bool"
                        ctx.code = expr1.code
                        ctx.code += f"i2f\n"
                        ctx.code += expr2.code
                    elif expr1.exprType == "float" and expr2.exprType == "int":
                        ctx.exprType = "bool"
                        ctx.code = expr1.code
                        ctx.code += expr2.code
                        ctx.code += f"i2f\n"
                    else:
                        exit(f"line {line}:{column} Cannot compare {expr1.exprType} with {expr2.exprType}")

                    if expr1.exprType == "float" or expr2.exprType == "float":
                        ctx.code += self.createBooleanStructure(isInAttribution, isFloat=True)
                        ctx.code = ctx.code.replace("_op_", f"if{self.translateOperatorJasmin(op)}", 1)
                    elif expr1.exprType == "str":
                        ctx.code += f"invokevirtual java/lang/String/equals(Ljava/lang/Object;)Z\n"
                        ctx.code += f"iconst_1\n"
                        ctx.code += f"ixor\n"
                        ctx.code += self.createBooleanStructure(isInAttribution, isString=True)
                        ctx.code = ctx.code.replace("_op_", f"if{self.translateOperatorJasmin(op)}", 1)
                    else:
                        ctx.code += (f"if_{self.translateTypeJasmin(expr1.exprType, True).lower()}"
                                     f"cmp{self.translateOperatorJasmin(op)}")
                        ctx.code += self.createBooleanStructure(isInAttribution)

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
