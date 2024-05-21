class Player:
    def __init__(self, name, token):
        self.name = name
        self.token = token
        self.money = 1500
        self.position = 0
        self.collected = []
        self.x = 0
        self.y = 0
        self.direction = "right"

    def get_playerinfo(self):
        return self.name, self.token, self.money, self.position, self.collected

    def get_token(self):
        return self.token

    def new_position(self, new_position):
        self.position = new_position

    def get_position(self):
        return self.position

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_money(self):
        return self.money

    def add_money(self, money):
        self.money += money

    def remove_money(self, money):
        self.money -= money

    def add_collected(self, new_property):
        self.collected.append(new_property)

    def remove_collected(self, old_property):
        self.collected.remove(old_property)

    def get_collected(self):
        return self.collected


class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

    def get_prompt(self):
        return self.prompt

    def get_answer(self):
        return self.answer
