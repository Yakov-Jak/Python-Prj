# Складываем матрицы
class Matrix:
    def __init__(self, matr):
        self._str = len(matr)
        self._matr = matr
        self._stlb_len = []
        for i, el in enumerate(self._matr):
            self._stlb_len.append(len(el))

        if len(set(self._stlb_len)) == 1:
            print('Матрица заполнена верно')
        else:
            print('Матрица заполнена не верно. Проверьте количество элементов в каждой строке')
            exit()

    def __str__(self):
        for el in self._matr:
            print(el)
        return ''

    def __add__(self, other):
        # Проверяем размерность матриц для сложения
        if self._stlb_len[0] == other._stlb_len[0] and self._str == other._str:
            res = []
            for i, el in enumerate(self._matr):
                res_str = [x + y for x, y in zip(self._matr[i], other._matr[i])]
                res.append(res_str)
            return res

        else:
            print('Неверная размерность складываемых матриц')
            return ''

my_list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
my_list2 = [[2, 4, 6], [8, 10, 12], [14, 16, 18]]
a = Matrix(my_list1)
b = Matrix(my_list2)
c = a + b
print(c)

