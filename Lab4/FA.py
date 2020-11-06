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

        self.initialState = f.readline().split(" ")[0]

        self.finaleStates = f.readline().split(" ")
        self.finaleStates[-1] = self.finaleStates[-1].strip("\n")

        for line in f:
            list = line.split(" ")
            self.fa[(list[0], list[1])] = list[2]

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
            print("(" + key[0] + "," + key[1] + ")" + "-> " + self.fa[key])

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
