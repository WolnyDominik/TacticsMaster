import arcade


class Options(arcade.View):

    def __init__(self):
        super().__init__()

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