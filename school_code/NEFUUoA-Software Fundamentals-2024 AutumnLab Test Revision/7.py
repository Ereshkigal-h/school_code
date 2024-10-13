class Student:
    def __init__(self,surname,firstname,student_id,):
        self.__surname=surname
        self.__firstname=firstname
        self.__student_id=student_id
        self.__project_scores=[]
        self.average_score=0
    def __str__(self):
        return f"{self.__surname} {self.__firstname}({self.__student_id}), average score = {self.average_score}"
    def add_project_score(self,score):
        if score<10 and score>1:
            self.__project_scores+=[score]
            self.average_score=round(sum(self.__project_scores) / len(self.__project_scores), 1)
    def get_names(self):
        return f"{self.__surname} {self.__firstname}"
    def get_student_id(self):
        return self.__student_id
    def get_project_scores(self):
        return self.__project_scores
    def get_average(self):
        return self.average_score




