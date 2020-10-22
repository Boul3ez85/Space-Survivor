import arcade
import os
import random

SCREEN_WIDTH = 1366
SCREEN_HEIGHT = 768
SCREEN_TITLE = "Space Survivor"
SCALING = 5 / 7


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
        if self.right < 0:
            self.remove_from_sprite_lists()


class SpaceSurvivor(arcade.Window):
    """ Main application class."""

    def __init__(self, width, height, title):
        super().__init__(width, height, title, fullscreen=True)

        # makes sure to pull images from the same directory the source file is in.
        res = os.path.dirname(os.path.abspath(__file__))
        os.chdir(res)

        # Background image will be stored in this variable
        self.acc_time = None
        self.interval = None
        self.collision_sound = None
        self.background_music = None
        self.background = None
        self.paused = False
        self.game_over = False
        self.enemies_list = arcade.SpriteList()
        self.clouds_list = arcade.SpriteList()
        self.all_sprites = arcade.SpriteList()
        self.player = arcade.Sprite()

    def setup(self):
        """ Set up the game variables. Call to re-start the game. """

        self.background = arcade.load_texture("res/images/stars.background.png")

        self.player = arcade.Sprite("res/images/playerShip1_red.png", SCALING)
        self.player.angle = -90
        self.player.center_y = self.height / 2
        self.player.left = 0
        self.all_sprites.append(self.player)

        # set the time interval that enemies and clouds appears
        arcade.schedule(self.add_enemy, 0.4)
        arcade.schedule(self.add_cloud, 1)

        # play music in game
        self.background_music = arcade.load_sound(":resources:music/1918.mp3")

        # add collision sound
        self.collision_sound = arcade.load_sound(":resources:sounds/explosion1.wav")

    def play_background_music(self, delta_time: int = 0):
        """Starts playing the background music"""
        self.background_music.play()

    def add_enemy(self, delta_time: float):
        """Adds a new enemy to the screen
        Arguments:
            delta_time {float} -- How much time has passed since the last call
        """

        enemy = FlyingSprite("res/images/spaceMissiles_040.png")

        # Set its position to a random height and off screen right
        enemy.left = random.randint(self.width, self.width + 80)
        enemy.top = random.randint(10, self.height - 10)

        # Set its speed to a random speed heading left
        enemy.velocity = (random.randint(-7, -5), 0)

        # Add enemy to the enemies_list
        self.enemies_list.append(enemy)
        # Add enemy to the list of all_sprites.
        self.all_sprites.append(enemy)

    def add_cloud(self, delta_time: float):
        """Adds a new enemy to the screen
        Arguments:
            delta_time {float} -- How much time has passed since the last call
        """

        cloud = FlyingSprite("res/images/cloud1.png", SCALING)

        # Set its position to a random height and off screen right
        cloud.left = random.randint(self.width, self.width + 80)
        cloud.top = random.randint(10, self.height - 10)

        # Set its speed to a random speed heading left
        cloud.velocity = (random.randint(-4, -3), 0)

        # Add it to the enemies list
        self.clouds_list.append(cloud)
        self.all_sprites.append(cloud)

    def on_draw(self):
        """ Render the screen. """
        arcade.start_render()

        # Divide screen width/height by two to get the horizontal/vertical center of the screen
        arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT,
                                      self.background)

        self.enemies_list.draw()
        self.clouds_list.draw()
        self.player.draw()

        # if game is over is true
        if self.game_over:
            message = f"Game Over!"
            arcade.draw_text(message, self.width / 2, self.height / 2, arcade.color.RADICAL_RED, 50,
                             align="center", anchor_x="center", anchor_y="center")

        if self.paused:
            message1 = f"PAUSE"
            arcade.draw_text(message1, self.width / 2, self.height / 2, arcade.color.RADICAL_RED, 50,
                             align="center", anchor_x="center", anchor_y="center")

    def on_key_press(self, symbol: int, modifiers: int):
        """ Handle user keyboard input
        q or ESCAPE: Quit the game
        p or BACKSPACE: Pause/Unpause the game
        z/q/s/d: Move up, left, down and right
        Arrows : Move up, left, down and right

        Arguments:
            symbol {int}: Which key was pressed
            modifiers {int}: Which modifiers were pressed
        """

        if symbol == arcade.key.ESCAPE:
            # quit game window
            arcade.close_window()

        if symbol == arcade.key.P or symbol == arcade.key.SPACE:
            self.paused = not self.paused
            if self.paused:
                arcade.unschedule(self.add_enemy)
                arcade.unschedule(self.add_cloud)
            else:
                arcade.schedule(self.add_enemy, 0.4)
                arcade.schedule(self.add_cloud, 1)

        if symbol == arcade.key.Z or symbol == arcade.key.UP:
            # move player up
            self.player.change_y = 5

        if symbol == arcade.key.S or symbol == arcade.key.DOWN:
            # move player down
            self.player.change_y = -5

        if symbol == arcade.key.Q or symbol == arcade.key.LEFT:
            # move player forward
            self.player.change_x = -5

        if symbol == arcade.key.D or symbol == arcade.key.RIGHT:
            # move player backward
            self.player.change_x = 5

    def on_key_release(self, symbol: int, modifiers: int):
        """ cancel movement pressed by a given key in on_key_press function
        when the key is released
        Arguments:
            symbol {int}: Which key was pressed
            modifiers {int}: Which modifiers were pressed
        """

        if (symbol == arcade.key.Z
            or symbol == arcade.key.S
            or symbol == arcade.key.UP
            or symbol == arcade.key.DOWN
        ):
            self.player.change_y = 0

        if (symbol == arcade.key.Q
            or symbol == arcade.key.D
            or symbol == arcade.key.LEFT
            or symbol == arcade.key.RIGHT
        ):
            self.player.change_x = 0

    def on_update(self, delta_time: float):
        """ game logic: updating positions and statuses of all game objects.
            Arguments:
                delta_time {float}: Time since the last update
        """

        # if the game paused do nothing.
        if self.paused:
            return


        # disable movement pressed by key/arrows once the game is over
        if self.game_over:
            self.player.remove_from_sprite_lists()

        # check for collision
        if self.player.collides_with_list(self.enemies_list):
            arcade.play_sound(self.collision_sound)
            self.game_over = True

        for enemy in self.all_sprites:
            enemy.update()

        # Keep the player on screen
        if self.player.top > self.height:
            self.player.top = self.height

        if self.player.right > self.width:
            self.player.right = self.width

        if self.player.bottom < 0:
            self.player.bottom = 0

        if self.player.left < 0:
            self.player.left = 0


def main():
    """ Main method """
    game = SpaceSurvivor(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
