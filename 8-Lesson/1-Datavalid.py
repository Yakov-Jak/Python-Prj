# Работаем с датой
class Data:

    def __init__(self, dtn):
        self.dtn = dtn

    @classmethod
    def data_conv(cls, dta):
        cls.dta = dta.split('-')
        for el in cls.dta:
            print(int(el))

    @staticmethod
    def data_valid(dt_str):
        dt_list = dt_str.split('-')
        print('Введён неверный день месяца') if int(dt_list[0]) > 31 or int(dt_list[0]) < 0 else print(int(dt_list[0]))
        print('Введён неверный месяц') if int(dt_list[1]) > 12 or int(dt_list[1]) < 0 else print(int(dt_list[1]))
        print('Введён неверный день месяца') if int(dt_list[0]) > 2100 or int(dt_list[2]) < 1888 else print(int(dt_list[2]))


Data('19-11-1991')
Data.data_conv('20-12-2021')
Data.data_valid('111-12-2022')