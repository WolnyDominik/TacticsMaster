import arcade
import pyglet.gl as gl
from gameRes.button import Button


class Menu(arcade.View):

    def __init__(self, game_window: arcade.Window):
        super().__init__()
        self.window = game_window
        width = self.window.width/5
        height = self.window.height/10
        base_x = self.window.width/4
        base_y = self.window.height/2
        offset = 50
        btn_play = Button(base_x, base_y + height + offset, width, height, 'play')
        btn_options = Button(base_x, base_y, width, height, 'options')
        btn_exit = Button(base_x, base_y - height - offset, width, height, 'exit')

        background = arcade.Sprite('resources\\menu_blur.png', self.window.height/512,0,0,960,512)
        background.center_x = self.window.width/2
        background.center_y = self.window.height/2
        self.background = arcade.SpriteList()
        self.background.append(background)

        self.btns = {}
        self.btns['play'] = btn_play
        self.btns['options'] = btn_options
        self.btns['exit'] = btn_exit

    def setup(self, game_view):
        self.game_view = game_view

    def on_draw(self):
        arcade.start_render()
        #self.background.draw(**{'filter': gl.GL_NEAREST})
        self.background.draw()

        for btn in self.btns.values():
            btn.draw()

    def on_mouse_press(self, x, y, button, modifiers):
        pass

    def on_mouse_release(self, x, y, button, modifiers):
        if self.btns['exit'].detect_click(x, y):
            arcade.close_window()
        if self.btns['play'].detect_click(x, y):
            self.window.show_view(self.game_view)

    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        pass

    def on_update(self, delta_time):
        pass
