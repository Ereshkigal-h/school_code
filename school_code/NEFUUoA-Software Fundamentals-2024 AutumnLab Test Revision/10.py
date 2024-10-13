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
class Country:
    def __init__(self,country_name):
        self.__name=country_name
        self.__cities_list=[]
    def get_name(self):
        return self.__name
    def add_city(self,name,population=None,area=None):
        tmp_city=City(name,population,area)
        self.__cities_list+=[tmp_city]
    def get_total_population(self):
        sum1=0
        for i in range(len(self.__cities_list)):
            sum1+=self.__cities_list[i].get_population()
        self.total_population= float(sum1)
        return float(sum1)
    def get_total_area(self):
        sum1=0
        sum1=float(sum1)
        for i in range(len(self.__cities_list)):
            sum1+=self.__cities_list[i].get_area()
        self.total_area=sum1
        return sum1
    def get_population_density(self):
        self.get_total_population()
        self.get_total_area()
        a=self.total_population/self.total_area
        return round(a,2)
    def get_city(self,index):
        return self.__cities_list[index]
    def __str__(self):
        a=f"{self.__name}:\n"
        for i in range(len(self.__cities_list)):
            a+= str(self.__cities_list[i]) + "\n"
        a+=f'Population density = {self.get_population_density():.2f}'
        return a
