import arcade
from gameRes.helpers import calculate_letters
import pyglet.gl as gl


class Button():
    def __init__(self, center_x, center_y, width, height, text):
        self.center_x = center_x
        self.center_y = center_y
        self.width = width
        self.height = height
        self.text = arcade.SpriteList()
        self.txt_len = len(text) + 1
        letters = calculate_letters(text)
        self.scale = height/5 * 0.4
        for idx, letter in enumerate(letters, start=1):
            if letter != True:
                # Letter texture
                sprite = arcade.Sprite('resources\\ascii.png', self.scale,
                                       4*letter[0], 6*letter[1], 3, 5)

                # Letter position
                sprite.center_x = self.center_x + \
                    (idx - self.txt_len/2) * 4 * self.scale
                sprite.center_y = self.center_y

                # Save letter
                self.text.append(sprite)

    def draw(self):
        arcade.draw_rectangle_filled(
            self.center_x, self.center_y, self.width, self.height,
            arcade.color.GRAY)
        self.text.draw(**{'filter': gl.GL_NEAREST})

    def recalculate_position(self, center_x, center_y, width, height):
        self.center_x = center_x
        self.center_y = center_y
        self.width = width
        self.height = height
        self.scale = height/5 * 0.5
        for idx, sprite in enumerate(self.text, start=1):
            # Letter position
            sprite.center_x = self.center_x + \
                (idx - self.txt_len/2) * 4 * self.scale
            sprite.center_y = self.center_y

            # Letter scale
            sprite.scale = self.scale

    def detect_click(self, click_x, click_y):
        clicked_x = True if click_x > self.center_x - self.width / \
            2 and click_x < self.center_x + self.width/2 else False
        clicked_y = True if click_y > self.center_y - self.height / \
            2 and click_y < self.center_y + self.height/2 else False

        return clicked_x and clicked_y

    def change_txt(self, text):
        for _ in range(len(self.text)):
            self.text.pop()
        self.txt_len = len(text) + 1
        letters = calculate_letters(text)
        for idx, letter in enumerate(letters, start=1):
            if letter != True:
                # Letter texture
                sprite = arcade.Sprite('resources\\ascii.png', self.scale,
                                       4*letter[0], 6*letter[1], 3, 5)

                # Letter position
                sprite.center_x = self.center_x + \
                    (idx - self.txt_len/2) * 4 * self.scale
                sprite.center_y = self.center_y

                # Save letter
                self.text.append(sprite)
