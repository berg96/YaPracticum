new_mail = 0

def check_mail():
    if new_mail > 0:
        print('Пришло письмо, не пропусти!')
    else:
        print('Никто не пишет.')

check_mail()
new_mail = 1
check_mail()

def hello(name):
    print(name + ', приветствую тебя!')

hello('Максим')