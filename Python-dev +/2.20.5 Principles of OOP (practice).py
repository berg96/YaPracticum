class Bird:
    def __init__(self, name: str, size: str) -> None:
        self.name: str = name
        self.size: str = size

    def describe(self, full: bool = False) -> str:
        if full:
            return 'Unexpected Error'
        return f'Размер птицы {self.name} — {self.size}.'


class Parrot(Bird):
    def __init__(self, name: str, size: str, color: str) -> None:
        super().__init__(name, size)
        self.color: str = color

    def describe(self, full: bool = False) -> str:
        if full:
            return (
                f'Попугай {self.name} — заметная птица, '
                f'окрас её перьев — {self.color}, а размер — {self.size}. '
                'Интересный факт: попугаи чувствуют ритм, а вовсе не бездумно '
                'двигаются под музыку. Если сменить композицию, '
                'то и темп движений птицы изменится.'
            )
        return super().describe(full)

    def repeat(self, phrase: str) -> str:
        return f'Попугай {self.name} говорит: {phrase}.'


class Penguin(Bird):
    def __init__(self, name: str, size: str, genus: str) -> None:
        super().__init__(name, size)
        self.genus: str = genus

    def describe(self, full: bool = False) -> str:
        if full:
            return (
                f'Размер пингвина {self.name} из '
                f'рода {self.genus} — {self.size}. Интересный факт: '
                'однажды группа геологов-разведчиков похитила пингвинье яйцо, '
                'и их принялась преследовать вся стая, не пытаясь, '
                'впрочем, при этом нападать. Посовещавшись, '
                'похитители вернули птицам яйцо, и те отстали.'
            )
        return super().describe(full)

    def swimming(self) -> str:
        return f'Пингвин {self.name} плавает со средней скоростью 11 км/ч.'


kesha = Parrot('Ара', 'средний', 'красный')
kowalski = Penguin('Королевский', 'большой', 'Aptenodytes')
print(kesha.repeat('Кеша хороший!'))
print(kowalski.swimming())
