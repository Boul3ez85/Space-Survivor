import arcade
from arcade.draw_commands import Texture
import os
import PIL
import random


EXPLOSION_TEXTURE_COUNT = 60


class Explosionplayer(arcade.Sprite):
    """This class creates an explosion player ship animation"""

    def __init__(self, texture_list):
        super().__init__()

        self.current_texture = 0
        self.textures = texture_list

    def update(self):
        """update to the next animation frame"""
        self.current_texture += 1
        if self.current_texture < len(self.textures):
            self.set_texture(self.current_texture)
        else:
            self.remove_from_sprite_lists()
