from HashTable import Hashtable


class Scanner:
    def __init__(self, fileName):
        self.symbolTable = Hashtable(40)
        self.programInternalForm = []
        self.filename = fileName

        self.listOfTokens = []
        self.listOfOperators = ['+', '-', '*', '/', '%', '<', '<=', '=', '>=', '>',
                                '==', 'and', 'or', 'not', '!=']

        self.listOfSeparators = ['[', ']', '{', '}', '(', ')', ';', ' ', "\'"]

        self.listOfReservedWords = ["if", "else", "number", "while", "for", "boolean", "read::",
                                    "print::", "string", "start", "end"]
        self.readTokens("tokens.txt")

        self.input = ""

    def readTokens(self, fileName):
        f = open(fileName, "r")
        for token in f:
            self.listOfTokens.append(token[:-1])
        f.close()

    def printInput(self):
        print(self.splitInputSeparators())
        print("")
        print(self.splitInputOperators())
        print("")
        print(self.input)

    def isIdentifier(self, token):
        if token[0] not in "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM":
            return False
        for char in token[1:]:
            if char != "_" and char not in "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890":
                return False
        return True

    def isConstant(self, token):
        if token[0] == 0:
            return False
        for char in token:
            if char not in "1234567890":
                return False
        return True

    def isSeparator(self, char):
        return char in self.listOfSeparators

    def isOperator(self, char):
        return char in self.listOfOperators

    def isReservedWord(self, c):
        return c in self.listOfReservedWords

    def splitInputSeparators(self):
        # split for all delimiters
        separatedInput = []
        lastSeparator = 0
        for i in range(0, len(self.input)):
            if self.isSeparator(self.input[i]):
                if lastSeparator == 0:
                    separatedInput.append(self.input[lastSeparator:i])
                    separatedInput.append(self.input[i])
                elif i == len(self.input) + 1:
                    separatedInput.append(self.input[i])
                    separatedInput.append(self.input[lastSeparator + 1:i + 1])
                else:
                    separatedInput.append(self.input[lastSeparator + 1:i])
                    separatedInput.append(self.input[i])
                lastSeparator = i

        return separatedInput

    def splitInputOperators(self, separatedInput):
        # split for all operators to get constants and identifiers
        allTokens = []
        for word in separatedInput:
            lastOperator = 0
            for i in range(0, len(word)):

                if self.isOperator(word[i]):
                    if lastOperator == 0:
                        allTokens.append(word[lastOperator:i])
                        allTokens.append(word[i])
                    else:
                        allTokens.append(word[lastOperator + 1:i])
                        allTokens.append(word[i])
                    lastOperator = i

            if lastOperator == 0:
                allTokens.append(word)
            else:
                allTokens.append(word[lastOperator + 1:i + 1])
        return allTokens

    def scan(self):
        with open(self.filename, 'r') as file:
            lineNo = 0
            for line in file:
                lineNo = lineNo + 1

                self.input = line
                input = self.splitInputSeparators()
                program = self.splitInputOperators(input)
                for word in program:
                    if word.strip(" ") == "":
                        continue
                    if self.isOperator(word) or self.isSeparator(word) or self.isReservedWord(word):
                        self.programInternalForm.append([word, -1])

                    elif self.isIdentifier(word) or self.isConstant(word):
                        index = self.symbolTable.find(word)
                        if index == -1:
                            i = self.symbolTable.add(word)
                            self.programInternalForm.append([word, i])
                        else:
                            self.programInternalForm.append([word, index])
                    else:
                        raise Exception(
                            "Lexical error found! Invalid token '" + word + "'" + " at line: " + str(lineNo))

        print("Symbol Table: ")
        print(self.symbolTable)
        print("PIF: ")
        # for line in self.programInternalForm:
        #     print(line, '\n')
        print(self.programInternalForm)
        # print(self.listOfTokens)


def test():
    s = Scanner("pb2.txt")
    s.scan()


test()
