import arcade
import os


res = os.path.dirname(os.path.abspath(__file__))
os.chdir(res)


SCREEN_WIDTH = 1366
SCREEN_HEIGHT = 768
SCREEN_TITLE = "Space Survivor"


class YouwinView(arcade.View):
    """ Represent the You win view class"""
    def __init__(self, game_view):
        super().__init__()
        self.game_view = game_view
        self.background = None

    def on_show(self):
        self.background = arcade.load_texture("res/images/win.png")

    def on_draw(self):
        arcade.start_render()
        
        arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT,
                                      self.background)

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        from game import SpaceSurvivor
        game_view = SpaceSurvivor()
        game_view.setup()
        self.window.show_view(game_view)

    def on_key_press(self, key, _modifiers):
        if key == arcade.key.Q:
            arcade.close_window()
