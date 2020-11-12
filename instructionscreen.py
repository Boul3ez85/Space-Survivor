import arcade
import os
import random


res = os.path.dirname(os.path.abspath(__file__))
os.chdir(res)


SCREEN_WIDTH = 1366
SCREEN_HEIGHT = 768
SCREEN_TITLE = "Space Survivor"
SCALING = 1 / 3


class FlyingSprite(arcade.Sprite):
    """Base class for all flying sprites
       Flying sprites include enemies and clouds
    """

    def update(self):
        """Update the position of the sprite
        When it moves off screen to the left, remove it
        """

        # Move the sprite
        super().update()

        # Remove if off the screen
        if (
                self.velocity[0] < 0 and self.right < 0
                or self.velocity[0] > 0 and self.left > SCREEN_WIDTH
        ):
            self.remove_from_sprite_lists()

class InstructionView(arcade.View):
    def __init__(self):
        super().__init__()
        from game import SpaceSurvivor
        self.game_view = SpaceSurvivor()

        self.metorites_list = arcade.SpriteList()
        self.background = None
        arcade.schedule(self.add_metorite, 1)

    def on_show(self):
        self.background = arcade.load_texture("res/images/instructions.png")

    def add_metorite(self, delta_time: float):
        metorite = FlyingSprite("res/images/space_survivor-comet-2.webp", SCALING)

        metorite.left = random.randint(SCREEN_WIDTH, SCREEN_WIDTH + 80)
        metorite.top = random.randint(10, SCREEN_HEIGHT - 10)

        # Set its speed to a random speed heading left
        metorite.velocity = (random.randint(-10, -5), 0)

        # Add it to the enemies list
        self.metorites_list.append(metorite)


    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT,
                                      self.background)

        self.metorites_list.draw()

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        self.game_view.setup()
        self.window.show_view(game_view)

    def on_update(self, delta_time: float):
        self.metorites_list.update()
