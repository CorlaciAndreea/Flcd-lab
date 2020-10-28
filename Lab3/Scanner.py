from HashTable import Hashtable
import re


class Scanner:
    def __init__(self, fileName):
        self.symbolTable = Hashtable(40)
        self.programInternalForm = []
        self.filename = fileName
        self.listOfTokens = self.readTokens()

    def readTokens(self):
        tokens = []
        with open("tokens.txt") as file:
            for line in file:
                tokens.append(line.strip("\n"))
        return tokens

    def isIdentifier(self, token):
        if token[0] not in "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM":
            return False
        for char in token[1:]:
            if char != "_" and char not in "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890":
                return False
        return True

    def isConstant(self, token):
        pattern0 = re.compile("0")
        pattern1 = re.compile("[-]?[1-9]+[0-9]*")
        pattern2 = re.compile("\"[a-zA-Z0-9]+\"")
        return pattern0.match(token) or pattern1.match(token) or pattern2.match(token)

    def detect(self, line):
        line = line.strip("\t\n ")
        tokens = re.split('([^a-zA-Z0-9"-])', line)
        tokens = list(filter(lambda x: x != " " and x != "" and x != "\n" and x != "\t", tokens))
        return tokens

    def scan(self):
        with open(self.filename, 'r') as file:
            lineNo = 0
            for line in file:
                lineNo = lineNo + 1
                tokens = self.detect(line)
                for word in tokens:
                    if word in self.listOfTokens:
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

        f = open("out.txt", "w")
        f.write("Symbol Table: \n")
        f.write("Hashtable with linked lists\n")
        f.write(self.symbolTable.__str__())

        f.write("PIF: \n")
        f.write(self.programInternalForm.__str__())
        f.close()


def test():
    s = Scanner("pb2.txt")
    s.scan()


test()
