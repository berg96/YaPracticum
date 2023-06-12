class Bird:
    def __init__(self, name: str, size: str) -> None:
        self.name: str = name
        self.size: str = size

    def describe(self) -> str:
        return f'Размер птицы {self.name} — {self.size}.'


class Parrot(Bird):
    def __init__(self, name: str, size: str, color: str) -> None:
        super().__init__(name, size)
        self.color: str = color


class Penguin(Bird):
    def __init__(self, name: str, size: str, genus: str) -> None:
        super().__init__(name, size)
        self.genus: str = genus


kesha = Parrot('Ара', 'средний', 'красный')
kowalski = Penguin('Королевский', 'большой', 'Aptenodytes')
