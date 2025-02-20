class User():
    def __init__(self, id, name):
        self.__id = id
        self.__name = name
        self.__level_access = "user"

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_level_access(self):
        return self.__level_access

    def set_name(self, name):
        self.__name = name

    def __str__(self):
        return f"ID: {self.__id}, Имя: {self.__name}, Уровень доступа: {self.__level_access}"


class Admin(User):
    def __init__(self, id, name):
        super().__init__(id,name)
        self.level_access = "admin"

    def add_user(self,users_list, user):
        users_list.append(user)
        print("Пользователь добавлен:", user)

    def remove_user (self, users_list, user):
        users_list.remove(user)
        print("Пользователь удален:", user)

users_list = []

user1 = User ("n001", "Василий")
user2 = User ("n002", "Мария")
user3 = User ("n003", "Николай")
user4 = User ("n004", "Егор")
user5 = User ("n005", "Анна")

admin1 = Admin ("a001", "Александр")
admin2 = Admin ("a002", "Владимир")

print("Имя пользователя:", user2.get_name())
admin1.add_user(users_list, user1)
admin1.add_user(users_list, user2)
admin2.add_user(users_list, user3)
admin2.add_user(users_list, user4)

print("Список пользователей:")
for user in users_list:
    print(user)
