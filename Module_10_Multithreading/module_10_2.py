import threading
import time



class Knight(threading.Thread):

    def __init__(self, name, pwr):
        threading.Thread.__init__(self)
        self.name = name
        self.pwr = pwr

    def run(self):
        enemy = 100
        day = 1
        print(f"{self.name}, на нас напали!!!")
        while enemy:
            enemy -= self.pwr
            print(f"{self.name} сражается {day} дней..., осталось {enemy} войнов")
            day += 1
            time.sleep(1)
        print(f"{self.name} одержал победу спустя {day - 1} дней(дня)!")





first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()

while first_knight.is_alive() == True and second_knight.is_alive() == True:
    break
else:
    print("Все бои закончились!!!")