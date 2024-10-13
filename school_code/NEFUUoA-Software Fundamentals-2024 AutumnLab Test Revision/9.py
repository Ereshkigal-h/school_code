class City:
    def __init__(self,name,population=None,area=None):
        self.__name=name
        if population==None:
            self.__population=1
        else:
            self.__population=population
        if area==None:
            self.__area=1
        else:
            self.__area = area
    def get_name(self):
        return self.__name
    def get_population(self):
        return self.__population
    def get_area(self):
        return self.__area
    def __str__(self):
        return f"{ self.__name}({round(self.__population/self.__area,2):.2f})"
    def set_name(self,name):
        self.__name = name
    def set_population(self,population):
        if population >=0:
            self.__population = population
    def set_area(self,area):
        if area>=0:
            self.__area = area
    def get_population_density(self):
        return self.__population/self.__area