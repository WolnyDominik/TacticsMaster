import arcade
from ..gameRes.helpers import calculate_letters


class Button():
    def __init__(self, x=0, y=0, width=0, height=0, text=''):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.text_sprites = arcade.SpriteList()
        txt_len = len(text)
        letters = calculate_letters(text)
        for idx, letter in enumerate(letters, start=1):
            if letter != True:
                # Letter texture
                sprite = arcade.Sprite('resources\\ascii.png', 4, 4*letter[0],
                                       6*letter[1], 4, 5)

                # Letter position
                sprite.center_x = self.x + \
                    (self.width / 2) - ((txt_len / 2) + idx) * 4
                sprite.center_y = self.y + (self.height / 2)

                # Save letter
                self.text_sprites.append(sprite)

    def print(self):
        pass

    def draw(self):
        pass
