import arcade
from views.menu import Menu
from views.game import Game
from views.options import Options


if __name__ == '__main__':
    window = arcade.Window(fullscreen=True)
    game_view = Game(window)
    menu_view = Menu(window)
    menu_view.setup(game_view)
    game_view.setup(menu_view)
    window.show_view(menu_view)
    arcade.run()
