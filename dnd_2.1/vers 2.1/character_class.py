"""тут описывается основной состав класса "Персонаж". 
итоговый результат данного класса - собранный словарь все
данных персонажа"""


class Character: # переделать
    """класс который создает словарь инфы  персонажа"""

    def __init__(self, character_name, player_name, level,
                 race, main_class, alignment, background, stats, modificators):
        # приемка и сохранение данных
        self.character_name = character_name
        self.stats = stats
        self.background = background
        self.player_name = player_name
        self.main_class = main_class
        self.level = level
        self.race = race
        self.alignment = alignment
        self.modificators = modificators

    def character_info(self):
        """функция запаковывает всю инфу в словарь"""
        character = {
            "players_name": self.player_name,
            "character_name": self.character_name,
            "characteristics": self.stats,
            "modificators": self.modificators,
            "background": self.background,
            "class": self.main_class,
            "level": self.level,
            "race": self.race,
            "aligment": self.alignment
        }
        return character
