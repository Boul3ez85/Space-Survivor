import arcade
import os


res = os.path.dirname(os.path.abspath(__file__))
os.chdir(res)


SCREEN_WIDTH = 1366
SCREEN_HEIGHT = 768
SPRITE_SCALING = 0.5


class YouwinView(arcade.View):
    def __init__(self, game_view):
        super().__init__()
        self.game_view = game_view
        # Don't show the mouse cursor
        self.window.set_mouse_visible(True)

    def on_show(self):
        arcade.set_background_color(arcade.color.GREEN)
        # Don't show the mouse cursor
        self.window.set_mouse_visible(False)

    def on_draw(self):
        arcade.start_render()

        arcade.draw_text("Youhou..You Win", SCREEN_WIDTH/2, SCREEN_HEIGHT/2+50,
                         arcade.color.BLACK, font_size=50, anchor_x="center")


    def on_mouse_press(self, _x, _y, _button, _modifiers):
        from game import SpaceSurvivor
        game_view = SpaceSurvivor()
        game_view.setup()
        self.window.show_view(game_view)

    def on_key_press(self, key, _modifiers):
        if key == arcade.key.Q:
            arcade.close_window()


