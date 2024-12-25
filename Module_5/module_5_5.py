import time

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return f"{self.nickname}, {self.password}, {self.age}"

    def __eq__(self,other):
        return self.nickname == other.nickname

    def get_info(self):
        return self.nickname ,self.password

class Video:
    def __init__(self, title, duration, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

    def __repr__(self):
        return self.title

    def __str__(self):
        return self.title


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        for user in self.users:
            if (nickname, hash(password)) == user.get_info():
                self.current_user = user
                return user


       #############

    def register(self, nickname, password, age):
        new_user = User(nickname, password, age)
        if new_user not in self.users:
            self.users.append(new_user)
            self.current_user = new_user
        else:
            print(f"Пользователь {nickname} уже существует")




    def log_out(self):
        self.current_user = None


    #def add(self, *videos):
    #    for video in videos:
    #        if video.title in self.videos:
    #            print(f"Видео с таким названием уже существует")
    #        else:
    #            self.videos.append(video)

    def add(self, *videos:Video):
        for video in videos:
            if video.title not in self.videos:
                self.videos.append(video)
            else:
                print(f"Видео с таким названием уже существует")
    def get_videos(self, find):
        results = []
        for video in self.videos:
            if find.lower() in video.title.lower():
                results.append(video.title)
        return results

    def watch_video(self, title):
        if self.current_user is None:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return

        for video in self.videos:
            if video.title == title:
                if video.adult_mode is True and self.current_user.age < 18:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                else:
                    print(f"Просмотр видео: {video.title}")
                    while video.time_now < video.duration:
                        print(f"{video.time_now} сек")
                        time.sleep(1)
                        video.time_now += 1
                    print("Конец видео")
                    self.log_out()
            else:
                print(f"Видео: {title} не найдено")


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')