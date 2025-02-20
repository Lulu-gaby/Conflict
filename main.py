class User():
    def __init__(self, id, name):
        self.__id = id
        self._name = name
        self._level_access = "user"

    def get_id(self):
        return self.__id

    def get_name(self):
        return self._name

    def get_level_access(self):
        return self._level_access

    def set_name(self, name):
        self._name = name

    def __str__(self):
        return f"ID: {self.__id}, Имя: {self._name}, Уровень доступа: {self._level_access}"


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

user1 = User ("1-1", "Петр")
user2 = User ("1-2", "Светлана")
user3 = User ("1-3", "Ольга")

admin = Admin ("A-1", "Виктор")

print("Имя пользователя:", user2.get_name())
admin.add_user(users_list, user1)
admin.add_user(users_list, user2)

print("Список пользователей:")
for user in users_list:
    print(user)
