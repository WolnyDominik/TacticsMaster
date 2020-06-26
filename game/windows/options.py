import arcade


class Options(arcade.Window):

    def __init__(self, width=800, height=600, title='Arcade Window', 
                fullscreen=False, resizable=False, update_rate=1/60, 
                antialiasing=True):
        super().__init__(width=width, height=height, title=title, 
                        fullscreen=fullscreen, resizable=resizable, 
                        update_rate=update_rate, antialiasing=antialiasing)

    def setup(self):
        pass

    def on_draw(self):
        arcade.start_render()

    def on_mouse_press(self, x, y, button, modifiers):
        pass

    def on_mouse_release(self, x, y, button, modifiers):
        pass

    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        pass

    def on_update(self, delta_time):
        pass