class FiniteAutomaton:
    def __init__(self):
        # list of all the states
        self.states = []
        # the alphabet
        self.alphabet = []
        # initial state
        self.initialState = None
        # list of finale states
        self.finaleStates = []
        # dictionary with key a tuple of states
        self.fa = {}
        self.readFile()

    def readFile(self):
        f = open("fa.in", "r")

        self.states = f.readline().split(" ")
        self.states[-1] = self.states[-1].strip("\n")

        self.alphabet = f.readline().split(" ")
        self.alphabet[-1] = self.alphabet[-1].strip("\n")

        self.initialState = f.readline().split(" ")[0].strip("\n")

        self.finaleStates = f.readline().split(" ")
        self.finaleStates[-1] = self.finaleStates[-1].strip("\n")

        for line in f:
            list = line.split(" ")
            k = (list[0], list[1])
            if k not in self.fa.keys():
                self.fa[k] = []
            self.fa[k].append(list[2].strip("\n"))

    def menu(self):
        print()
        print("1- Print set of states")
        print("2- Print finite alphabet")
        print("3- Print initial state")
        print("4- Print finale state/states")
        print("5- Print set of transitions")
        print("0- Exit")
        print()

    def printStates(self):
        print("\nStates:")
        for state in self.states:
            print(state)

    def printAlphabet(self):
        print("\nThe alphabet:")
        for a in self.alphabet:
            print(a)

    def printInitialState(self):
        print("\nInitial state: " + self.initialState)

    def printFinalStates(self):
        print("\nFinal states:")
        for f in self.finaleStates:
            print(f)

    def printFA(self):
        print("\nTransitions:")
        for key in self.fa:
            for val in self.fa[key]:
                print("(" + key[0] + "," + key[1] + ")" + "-> " + val)

    def isDeterministic(self):
        for val in self.fa.values():
            if len(val) > 1:
                return False
        return True

    def check(self, sequence):
        if not self.isDeterministic():
            print("Fa not deterministic")
            return False
        current = self.initialState
        lens = len(sequence)
        ok = False
        for elem in sequence:
            ok = False
            for trans in self.fa.keys():
                if self.fa[trans][0] == elem and current == trans[0]:
                    ok = True
                    current = trans[1]
                    break
            if not ok:
                break
            else:
                lens -= 1
        if current in self.finaleStates and lens == 0:
            return True
        else:
            return False

    def start(self):
        while True:
            self.menu()
            command = int(input("Enter command:"))
            if command == 1:
                self.printStates()
            elif command == 2:
                self.printAlphabet()
            elif command == 3:
                self.printInitialState()
            elif command == 4:
                self.printFinalStates()
            elif command == 5:
                self.printFA()
            elif command == 0:
                break
            else:
                print("\n Wrong command")


fa = FiniteAutomaton()
fa.start()
print(fa.check("abcddddd"))
print(fa.check("abbbcd"))
