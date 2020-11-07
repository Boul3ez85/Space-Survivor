import arcade
import os


res = os.path.dirname(os.path.abspath(__file__))
os.chdir(res)


SCREEN_WIDTH = 1366
SCREEN_HEIGHT = 768
SPRITE_SCALING = 0.5


class InstructionView(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.ORANGE_PEEL)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Instructions", SCREEN_WIDTH/2, SCREEN_HEIGHT/2,
                         arcade.color.BLACK, font_size=50, anchor_x="center")
        arcade.draw_text("Click to play", SCREEN_WIDTH/2, SCREEN_HEIGHT/2-75,
                         arcade.color.GRAY, font_size=20, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        from game import SpaceSurvivor
        game_view = SpaceSurvivor()
        game_view.setup()
        self.window.show_view(game_view)
