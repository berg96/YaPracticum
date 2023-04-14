english = {
    'рука': 'hand',
    'нога': 'leg',
    'хвост': 'tail',
    'питон': 'python',
    'бэкенд-разработчик': 'backend developer'
}

print(english['рука'])
english['рука'] = 'arm'
print(english['рука'])
words_ru = list(english.keys())
words_en = list(english.values())
print(words_ru)
print(words_en)