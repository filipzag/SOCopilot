class Process():

    def __init__(self, name, id, parent_id):
        self.__name = name
        self.__id = id
        self.__parent_id = parent_id
        self.__children = None

    def get_name(self):
        return self.__name

    def get_id(self):
        return self.__id

    def get_parent(self):
        return self.__parent_id


    def add_child(self, child_name):
       if self.__children:
           self.__children.append(child_name)
       else:
           self.__children = [child_name]

    def get_children(self):
        return self.__children


