class Node():

    def __init__(self, val):
        self.__val = val
        self.__next = None

    def get_data(self):
        return self.__val

    def set_data(self, val):
        self.__val = val

    def get_next(self):
        return self.__next

    def set_next(self, next):
        self.__next = next



class LinkedList():

    def __init__(self, head = None):
        self.__head = head
        self.__count = 0

    

    def get_head(self):
        return self.__head



    def insert(self, data):

        new_node = Node(data)

        new_node.set_next(self.__head)

        self.__head = new_node

        self.__count += 1



    def find (self, sval):
    
        item = self.__head


        while item != None:

            if item.get_data() == sval:
                return item
            else:
                item = item.get_next()

        return None



    def get_count(self):
        return self.__count
