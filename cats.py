class Cats:
    def __init__(self, name, gender, age):
        self.name = f"Кличка котяу: {name}"
        self.gender = f"Пол: {gender}"
        self.age = f"Возраст: {age} года"

    def get_name(self):
        return self.name

    def get_gender(self):
        return self.gender

    def get_age(self):
        return self.age
