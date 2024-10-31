class Database:
    def __init__(self):
        self.data = {}

    def add_user(self, username, password):
        self.data[username] = password


class User:
    """
    Класс ппорльзователя, содержащий атрибуты: логин, пароль
    """

    def __init__(self, username, password, password_confim):
        self.username = username
        if password == password_confim:
            self.password = password


if __name__ == "__main__":
    database = Database()
    while True:
        choice = int(input("Приветствую! Выберите действие: \n1 - Вход\n2 - Регистрация\n"))
        if choice == 1:
            login = input("Enter username: ")
            password = input("Enter password: ")
            if login in database.data:
                if password == database.data[login]:
                    print(f'Вход выполнен, {login}')
                    break
                else:
                    print("Неверный пароль")
                    break
                print("ok")
            else:
                print("Неверный логин или пароль")
                break
        if choice == 2:
            user = User(input("Enter username: "), password := input("Enter password: "),
                        password2 := input("Confirm password: "))
            if password != password2:
                print("Пароли не совпадают, попробуйте снова")
                continue
            database.add_user(user.username, user.password)
        print(database.data)
