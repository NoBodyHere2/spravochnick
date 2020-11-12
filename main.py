# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
def emailIsValid():
    return True


class Guide:
    slovar = {}

    # ['email'] = ['имя','фамилия','телефон','город']

    def addNote(self, email, name, secName, number, city):
        if email not in self.slovar.keys():
            if (emailIsValid):
                self.slovar[email] = [name, secName, number, city]

    def change(self, email, name, secName, number, city):
        if email not in self.slovar.keys():
            return
        if len(str(name)):
            self.slovar[email][0] = name
        if len(str(secName)):
            self.slovar[email][1] = secName
        if len(str(number)):
            self.slovar[email][2] = number
        if len(str(city)):
            self.slovar[email][3] = city

    def find(self, email):
        if email not in self.slovar.keys():
            return
        return self.slovar[email]

    def delete(self, email):
        if email not in self.slovar.keys():
            return
        self.slovar.pop(email)


guide = Guide()

guide.addNote('whewisa@mail.com', 'Иван', 'Иванович', '1234567890', 'Москва')
guide.addNote('abc@mail.com', 'Алена', 'Виноградова', '88005553535', 'Челябинск')
print(guide.slovar)
guide.change('abc@mail.com', '', 'Lalala', '', '')
print(guide.slovar)

print(guide.find('abc@mail.com'))
print(guide.find('qabc@mail.com'))

guide.delete('abc@mail.com')
print(guide.slovar)

guide.delete('abc@mail.com')
print(guide.slovar)
