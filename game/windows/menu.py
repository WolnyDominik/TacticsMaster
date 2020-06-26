import arcade
from gameRes.button import Button

class Menu(arcade.Window):

    def __init__(self, width=800, height=600, title='Arcade Window', 
                fullscreen=False, resizable=False, update_rate=1/60, 
                antialiasing=True):
        super().__init__(width=width, height=height, title=title, 
                        fullscreen=fullscreen, resizable=resizable, 
                        update_rate=update_rate, antialiasing=antialiasing)
        btn_play = Button(100, 100, 150, 40, 'play')
        btn_options = Button(100, 160, 150, 40, 'options')
        btn_exit = Button(100, 220, 150, 40, 'exit')

        arcade.set_background_color(arcade.color.WHITE)

        self.btns = []
        self.btns.append(btn_play)
        self.btns.append(btn_options)
        self.btns.append(btn_exit)

    def setup(self):
        pass

    def on_draw(self):
        arcade.start_render()

        for btn in self.btns:
            btn.draw()      

    def on_mouse_press(self, x, y, button, modifiers):
        pass

    def on_mouse_release(self, x, y, button, modifiers):
        pass

    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        pass

    def on_update(self, delta_time):
        pass