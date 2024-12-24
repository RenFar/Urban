import time

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age

    def __str__(self):
        return f"{self.nickname}, {self.password}, {self.age}"

class Video:
    def __init__(self, title, duration, time_now = 0, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adulut_mode = adult_mode

class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname:
                self.current_user = user


       #############

    def register(self, nickname, password, age):
        for user in self.users:
            print(self.users, "123")
            if user.nickname == nickname:
                print(f"Пользователь {nickname} уже существует")
                return

        user = User(nickname, password, age)
        print(self.users, "321")
        self.users.append(user)
        self.log_in(nickname, password)
        print(self.users, "321")

    def log_out(self):
        self.current_user = None


    #def add(self, *videos):
    #    for video in videos:
    #        if video.title in self.videos:
    #            print(f"Видео с таким названием уже существует")
    #        else:
    #            self.videos.append(video)

    def add(self, *videos):
        for video in videos:
            if video.title not in [v.title for v in self.videos]:
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
        else:
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