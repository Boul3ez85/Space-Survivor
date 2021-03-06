import arcade
import os


SCREEN_WIDTH = 1366
SCREEN_HEIGHT = 768
SCREEN_TITLE = "Space Survivor"


res = os.path.dirname(os.path.abspath(__file__))
os.chdir(res)


class GameOverView(arcade.View):
    def __init__(self, game_view):
        super().__init__()
        self.game_view = game_view
        self.time_taken = 0
        self.background_image = None

    def on_show(self):
        self.background_image = arcade.load_texture("res/images/gameover.png")


    def on_draw(self):
        arcade.start_render()
        """
        Draw "Game over" across the screen.
        """
        arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT,
                                      self.background_image)


        arcade.draw_text("Click to restart", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 150, arcade.color.WHITE, 24, anchor_x="center")

        arcade.draw_text("Or press Q to quit", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 200, arcade.color.WHITE, 18, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        self.game_view.setup()
        self.window.show_view(self.game_view)

    def on_key_press(self, key, _modifiers):
        if key == arcade.key.Q:
            arcade.close_window()
