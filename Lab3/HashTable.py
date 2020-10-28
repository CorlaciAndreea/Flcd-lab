class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return "value:" + str(self.value) + " next: " + str(self.next)


class Hashtable:
    def __init__(self, size):
        self._table = [None] * size
        self._size = size

    def __str__(self):
        s = ""
        for symbol in self._table:
            s += str(symbol) + "\n"
        return s

    def hashFunction(self, key):
        return key % len(self._table)

    def asciiCode(self, elem):
        s = 0
        elem.strip("\"")
        for i in range(0, len(elem)):
            s = s + ord(elem[i])
        return s

    def add(self, value):
        if isinstance(value, str):
            key = self.asciiCode(value)
        else:
            key = value

        index = self.hashFunction(key)
        node = self._table[index]

        if node is None:
            self._table[index] = Node(value)
            return index
        # Iterate to the end of the linked list at provided index
        prev = node
        while node is not None:
            prev = node
            node = node.next

        prev.next = Node(value)
        return index

    def find(self, value):
        if isinstance(value, str):
            key = self.asciiCode(value)
        else:
            key = value

        index = self.hashFunction(key)


        if self._table[index] is None:
            return -1
        else:
            node = self._table[index]
            while node is not None:
                if node.value == value:
                    return index
                node = node.next

# def test():
#     st = Hashtable(10)
#
#     print(st.add("s"))
#     print(st.add("ab"))
#     st.add("c")
#     st.add("ba")
#     st.add("t")
#
#     print("Symbol table: \n")
#     print(st)
#
#     print("search 'ab':", st.find("ab"))
#
#     print("search 't':", st.find("t"))
#
#     print("search 'r':", st.find("r"))
#
#
# test()
