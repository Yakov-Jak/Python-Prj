# Работает светофором
from time import sleep
class Trfl:
    __color = 'red'

    def running(self):
        # self.__color = __color
        print(Trfl.__color)
        if Trfl.__color == 'red':
            Trfl.__color = 'yellow'
            sleep(7)
        elif Trfl.__color == 'yellow':
            Trfl.__color = 'green'
            sleep(2)
        elif Trfl.__color == 'green':
            Trfl.__color = 'red'
            sleep(5)
        else:
            print('Error')

a = Trfl()
a.running()
a.running()
a.running()
a.running()

