class Student:
    def __init__(self, student_number, first_name, last_name, date_of_birth, sex, country_of_birth):
        self.__student_number = student_number
        self.__first_name = first_name
        self.__last_name = last_name
        self.__date_of_birth = date_of_birth
        self.__sex = sex
        self.__country_of_birth = country_of_birth

    # Getter methods
    def get_student_number(self):
        return self.__student_number

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_date_of_birth(self):
        return self.__date_of_birth

    def get_sex(self):
        return self.__sex

    def get_country_of_birth(self):
        return self.__country_of_birth

    # Setter methods
    def set_student_number(self, student_number):
        self.__student_number = student_number

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def set_date_of_birth(self, date_of_birth):
        self.__date_of_birth = date_of_birth

    def set_sex(self, sex):
        self.__sex = sex

    def set_country_of_birth(self, country_of_birth):
        self.__country_of_birth = country_of_birth


classroom = [None] * 100