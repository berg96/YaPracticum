def check_mail():
    if new_mail > 0:
        print("Пришло письмо, не пропусти!")
    else:
        print("Никто не пишет.")

new_mail = 0
check_mail()
new_mail = 1
check_mail()


def hello(name):
    print(name + ", приветствую тебя!")

hello("Максим")


def hello(name, bonus):
    print(name + ", приветствую тебя! Бери " + bonus)

hello("Дарт Вейдер", "печеньки")
hello("Винни Пух", "мёд")


def print_home(name='Инкогнито', planet='Икс'):
    print(name + ' живёт на планете ' + planet)

print_home(planet='Земля')  