import arcade
import os


res = os.path.dirname(os.path.abspath(__file__))
os.chdir(res)


SCREEN_WIDTH = 1366
SCREEN_HEIGHT = 768
SPRITE_SCALING = 0.5


class PauseView(arcade.View):
    def __init__(self, game_view):
        super().__init__()
        self.game_view = game_view
        self.player = arcade.Sprite()

    def on_show(self):
        arcade.set_background_color(arcade.color.ORANGE)

    def on_draw(self):
        arcade.start_render()

        # Draw player, for effect, on pause screen.
        # The previous View (GameView) was passed in
        # and saved in self.game_view.
        self.player = self.game_view.player
        self.player.draw()

        # draw an orange filter over him
        arcade.draw_lrtb_rectangle_filled(left=self.player.left,
                                          right=self.player.right,
                                          top=self.player.top,
                                          bottom=self.player.bottom,
                                          color=arcade.color.ORANGE + (200,))


        arcade.draw_text("PAUSED", SCREEN_WIDTH/2, SCREEN_HEIGHT/2+50,
                         arcade.color.BLACK, font_size=50, anchor_x="center")

        # Show tip to return or reset
        arcade.draw_text("Press Esc. to return",
                         SCREEN_WIDTH/2,
                         SCREEN_HEIGHT/2,
                         arcade.color.BLACK,
                         font_size=20,
                         anchor_x="center")
        arcade.draw_text("Press Enter to reset",
                         SCREEN_WIDTH/2,
                         SCREEN_HEIGHT/2-30,
                         arcade.color.BLACK,
                         font_size=20,
                         anchor_x="center")


    def on_key_press(self, key, _modifiers):
        from game import SpaceSurvivor
        if key == arcade.key.P:   # resume game
            self.window.show_view(self.game_view)
            self.game_view.toggle_pause()
            # arcade.schedule(self.add_enemy, 1)
            # arcade.schedule(self.add_cloud, 3)
            #self.projectile_sound.stop()
        elif key == arcade.key.ENTER:  # reset game
            game_view = SpaceSurvivor()
            game_view.setup()
            self.window.show_view(game_view)
