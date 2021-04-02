class antri():

    def __init__(self):
        self.__data = []

    def namBel(self, data):
        self.__data.append(data)

    def kurDep(self):
        try:
            return self.__data.pop(0)
        except IndexError as e:
            return None
    
    def lihat(self):
        return self.__data[0]
    
    def sisa(self):
        return self.__data

    def juml(self):
        return len(self.__data)