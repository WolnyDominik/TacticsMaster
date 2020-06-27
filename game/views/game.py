import arcade


class Game(arcade.View):

    def __init__(self, game_window: arcade.Window):
        super().__init__()
        self.window = game_window
        #self.menu_view
        

    def setup(self, menu_view):
        self.menu_view = menu_view

    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color(arcade.color.AERO_BLUE)

    def on_mouse_press(self, x, y, button, modifiers):
        pass

    def on_key_release(self, _symbol, _modifiers):
        if _symbol == arcade.key.ESCAPE:
            self.window.show_view(self.menu_view)

    def on_mouse_release(self, x, y, button, modifiers):
        pass

    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        pass

    def on_update(self, delta_time):
        pass
