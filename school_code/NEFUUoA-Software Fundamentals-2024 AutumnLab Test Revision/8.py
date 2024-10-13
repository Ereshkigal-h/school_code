import copy


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
    def add_average(self,score):
            self.__project_scores+=[score]
            self.average_score=round(sum(self.__project_scores)/len(self.__project_scores),1)


class Project:
    def __init__(self,id,title):
        self.__students = []
        self.__project_id=id
        self.__title=title
    def get_project_id(self):
        return self.__project_id
    def get_title(self):
        return self.__title
    def add_student(self,student):
        self.__students+=[student]
    def get_number_of_students(self):
        return len(self.__students)
    def get_students(self):
        result=""
        for i in range(len(self.__students)):
            if i !=len(self.__students)-1:
                result+= str(self.__students[i].get_names()) + ","
            else:
                result += str(self.__students[i].get_names())
        return result
    def __str__(self):
        return f'ID={self.__project_id},({self.__title}):{self.get_students()}'
    def set_score(self,score):
        for i in range(len(self.__students)):
            self.__students[i].add_average(score)
