import arcade
from gameRes.helpers import calculate_letters
import pyglet.gl as gl


class Button():
    def __init__(self, x=0, y=0, width=0, height=0, text=''):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = arcade.SpriteList()
        self.txt_source = text
        txt_len = len(text) + 1
        letters = calculate_letters(text)
        #print(txt_len)
        for idx, letter in enumerate(letters, start=1):
            if letter != True:
                # Letter texture
                sprite = arcade.Sprite('resources\\ascii.png', 4, 4*letter[0],
                                       6*letter[1], 3, 5)

                # Letter position
                sprite.center_x = self.x + (idx - txt_len/2) * 16
                sprite.center_y = self.y

                # Save letter
                self.text.append(sprite)

    def draw(self):
        #arcade.start_render()

        arcade.draw_rectangle_filled(
            self.x, self.y, self.width, self.height, arcade.color.GRAY)
        self.text.draw(**{'filter': gl.GL_NEAREST})

    def recalculate_position(self):
        pass
